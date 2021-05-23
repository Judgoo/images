import os
from os import listdir, remove
from os.path import isfile, join
from typing import List

from generator import *  # noqa: F401
from generator.helper.base import BaseDockerFile


def gen(build_tool):
    _s = {k: v for k, v in globals().items() if hasattr(v, "ALL_IMAGES")}

    all_images: List[BaseDockerFile] = []

    for k, v in _s.items():
        all_images.extend(v.ALL_IMAGES)

    all_images.sort(key=lambda k: k.get_img_name())

    for f in listdir("./images"):
        if f.endswith(".base"):
            continue
        p = join("./images", f)
        if isfile(p):
            remove(p)

    build_sh = f"./build-images-{build_tool}.sh"
    build_all = f"./build-all-{build_tool}.sh"
    push_all = f"./push-all-{build_tool}.sh"

    with open(build_sh, "w+") as f:
        for image in all_images:
            image.generate_files()
            f.write(image.get_build_command(build_tool=build_tool))
            f.write("\n")
            f.flush()
    os.chmod(build_sh, 0o0777)

    if build_tool == "docker":
        with open(push_all, "w+") as f:
            for image in all_images:
                f.write(f"{build_tool} push {image.get_img_name()}")
                f.write("\n")
                f.flush()
        os.chmod(push_all, 0o0777)

    if build_tool == "docker":
        build_tool = "sudo docker"

    with open(build_all, "w+") as f:
        f.writelines(
            [
                f"{build_tool} build -t judgoo/base-alpine:v0.0.1 -f ./base/Dockerfile.alpine.base ./base\n",
                f"{build_tool} build -t judgoo/base-debian:v0.0.1 -f ./base/Dockerfile.debian.base ./base\n",
                "\n",
                f"sh {build_sh}\n",
            ]
        )

    os.chmod(build_all, 0o0777)


gen("docker")
gen("podman")
