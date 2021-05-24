import os
from os import listdir, remove
from os.path import isfile, join
from typing import List

from generator import *  # noqa: F401
from generator.helper.base import BaseDockerFile

_s = {k: v for k, v in globals().items() if hasattr(v, "ALL_IMAGES")}

all_images: List[BaseDockerFile] = []

for k, v in _s.items():
    all_images.extend(v.ALL_IMAGES)

for f in listdir("./images"):
    p = join("./images", f)
    if isfile(p):
        remove(p)

all_images.sort(key=lambda k: k.get_img_name())
for image in all_images:
    image.generate_files()

push_all = "./push-all-docker.sh"

with open(push_all, "w+") as f:
    for image in all_images:
        if not image._is_add_judger:
            image.add_judger()
        f.write(f"docker push {image.get_img_name()}")
        f.write("\n")
        f.flush()
os.chmod(push_all, 0o0777)


def gen(build_tool):
    build_sh = f"./build-images-{build_tool}.sh"
    build_all = f"./build-all-{build_tool}.sh"
    print(f"generate {build_tool} related..")
    with open(build_sh, "w+") as f:
        for image in all_images:
            f.write(image.get_build_command(build_tool=build_tool))
            f.write("\n")
            f.flush()
    os.chmod(build_sh, 0o0777)

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
