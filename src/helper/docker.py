"""
Copyright 2019 Jen-soft
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
"""
code is original from <https://github.com/jen-soft/pydocker>
"""

import json
import logging
import os
import re
import subprocess
import sys
from typing import Any, List, TypedDict, Union

log = logging.getLogger(__name__)


class Instruction(TypedDict):
    type: str
    name: str
    value: str


class DockerFile(object):
    FROM: Any
    LABEL: Any
    COPY: Any
    RUN: Any
    WORKDIR: Any
    ENV: Any
    SHELL: Any
    EXPOSE: Any
    ENTRYPOINT: Any
    CMD: Any
    ADD: Any
    STOPSIGNAL: Any
    USER: Any
    VOLUME: Any
    ARG: Any
    ONBUILD: Any
    HEALTHCHECK: Any

    _regex = re.compile(
        r"(?P<namespace>[0-9A-Za-z-\_\.]+)/"
        r"(?P<name>[0-9A-Za-z\-\_\.]+):"
        r"(?P<version>[0-9A-Za-z\-\_\.]+)"
    )
    _instructions: List[Instruction]

    def __init__(self, base_img, name, **kwargs):
        self._instructions = []
        if isinstance(base_img, DockerFile):
            base_img = base_img.get_img_name()
        self._instructions.append(
            {
                "type": "instruction",
                "name": "FROM",
                "value": base_img,
            }
        )
        # parse new img name
        _r = self._regex.search(name.strip())
        if _r is None:
            raise ValueError(
                'invalid img name "{}", ' 'should be as "local/base:0.0.1"'.format(name)
            )
        self._image_namespace = _r.group("namespace")
        self._image_name = _r.group("name")
        self._image_version = _r.group("version")
        self._build_args = kwargs.pop("build_args", "")

    def get_img_name(self):
        return "{}/{}:{}".format(
            self._image_namespace, self._image_name, self._image_version
        )

    def __setattr__(self, key, value):
        if key.startswith("_"):
            return super(DockerFile, self).__setattr__(key, value)
        if not isinstance(value, str):
            value = json.dumps(value)
        self._instructions.append(
            {
                "type": "instruction",
                "name": key,
                "value": value.strip(),
            }
        )

    def __repr__(self) -> str:
        return f"<Dockerfile {self.get_img_name()}>"

    def LABEL_(self, *args, **kwargs):
        assert not args
        #
        for k, v in kwargs.items():
            self.__setattr__("LABEL", '{}="{}"'.format(k, v))

    def add_new_file(self, dst_path, content, chmod=None):
        content = content.strip() + "\n"
        self._instructions.append(
            {
                "type": "file",
                "name": dst_path,
                "value": content,
            }
        )
        if chmod is not None:
            self.RUN = "chmod {} {}".format(chmod, dst_path)

    def COPY_(self, dst_path, content, chmod=None):
        self.add_new_file(dst_path, content, chmod=chmod)

    def RUN_bash_script(self, dst_path, content, keep_file=False):
        # https://stackoverflow.com/questions/22009364/is-there-a-try-catch-command-in-bash
        # https://unix.stackexchange.com/questions/462156/how-do-i-find-the-line-number-in-bash-when-an-error-occured
        content = (
            """
#!/usr/bin/env bash
set -e -o xtrace
function _failure() {
  echo -e "\\r\\nERROR: bash script [ %(script_name)s ] failed at line $1: \\"$2\\""
}
trap '_failure ${LINENO} "$BASH_COMMAND"' ERR
# ############################################################################ #
        """.strip()
            % {"script_name": dst_path}
            + "\n\n"
            + content
        )

        self.COPY_(dst_path, content, chmod="+x")
        self.RUN = dst_path
        if not keep_file:
            self.RUN = "rm {}".format(dst_path)

    def RUN_python_script(
        self, dst_path, fn, keep_file=False, python="/usr/bin/python"
    ):
        if not isinstance(fn, str):
            from inspect import getsource

            fn = "{}\n{}()".format(getsource(fn), fn.__name__)
        self.COPY_(dst_path, "# -*- coding: utf-8 -*-\n" + fn, chmod="+x")
        self.RUN = "{} {}".format(python, dst_path)
        if not keep_file:
            self.RUN = "rm {}".format(dst_path)

    def _get_dockerfile(self, dockerfile_name=None):
        if dockerfile_name is None:
            dockerfile_name = "Dockerfile.{}".format(self._image_name)

        result = ""
        files = []
        for instruction in self._instructions:
            if instruction["type"] == "file":
                dst_path = instruction["name"]
                local_name = "{}.{}@{}".format(
                    dockerfile_name, len(files), os.path.basename(dst_path)
                )
                files.append([local_name, instruction["value"]])
                result += "\nCOPY {} {}".format(local_name, dst_path)
            elif instruction["type"] == "instruction":
                result += "\n{name} {value}".format(**instruction)
            else:
                raise ValueError("invalid instruction type {}".format(instruction))

        files = [
            [dockerfile_name, result],
        ] + files
        return files

    def generate_files(
        self, dockerfile_name=None, path="./", remove_old_files=True, dry_run=False
    ):
        files = self._get_dockerfile(dockerfile_name)

        return self._create_files(path, files, remove_old_files, dry_run)

    def _create_files(self, path, files, remove_old_files, dry_run=False):
        dockerfile_name = files[0][0]
        if not dry_run:
            log.info(f"Generate dockerfile: {dockerfile_name}")
        if not dry_run and remove_old_files:
            for name in os.listdir(path):
                if re.findall(r"^{}.[0-9]+@".format(dockerfile_name), name):
                    os.remove(name)

        result_files = []
        for name, content in files:
            file_path = os.path.join(path, name)
            if not dry_run:
                with open(file_path, "w+") as file:
                    file.write(content.strip("\n"))
                    file.flush()
            result_files.append(file_path)
        return result_files

    def get_build_command(
        self, files=None, build_tool="", build_args="", trailing_args=""
    ):
        if files is None:
            files = self.generate_files(dry_run=True)
        dirname, filename = os.path.split(files[0])
        build_args = self._build_args.strip() + " " + build_args.strip()
        if build_tool == "docker":
            build_tool = "sudo docker"
        cmd = f'{build_tool} build {build_args}  --tag {self.get_img_name()}  --file={files[0]} "{dirname}/" {trailing_args}'
        cmd = re.sub(r"[\r\n\s\t]+", " ", cmd).strip()
        return cmd

    def build_img(self, remove_out_files=True):
        log.info("Build new docker img {}".format(self.get_img_name()))
        files = self.generate_files(dry_run=True)
        cmd = self.get_build_command(files)
        log.info('Execute "{}"'.format(cmd))
        p = subprocess.Popen(
            [
                cmd,
            ],
            shell=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
            stdin=subprocess.PIPE,
        )
        p.communicate()
        if remove_out_files and p.returncode == 0:
            for file in files:
                os.remove(file)

    def add_front_from(self, from_: str):
        self.FROM = from_
        x = self._instructions.pop()
        self._instructions.insert(0, x)

    def add_builder(self, Builder: Union["DockerFile", str], builder_name: str):
        if isinstance(Builder, str):
            self.add_front_from(f"{Builder} as {builder_name}")
        else:
            Builder._instructions[0]["value"] += f" as {builder_name}"
            self._instructions = Builder._instructions + self._instructions
