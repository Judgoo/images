import os
from os import listdir, remove
from os.path import isfile, join
from typing import List

from generator import *  # noqa: F401
from generator.helper.base import BaseDockerFile

build_tool = "docker"

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
f = open(build_sh, "w+")

for image in all_images:
    image.generate_files()
    f.write(image.get_build_command(build_tool=build_tool))
    f.write("\n")
    f.flush()

f.close()
if build_tool == "docker":
    build_tool = "sudo docker"

with open(build_all, "w+") as f:
    f.writelines(
        [
            f"{build_tool} build -t judgoo/base-alpine:v0.0.1 -f ./images/Dockerfile.alpine.base ./images\n",
            f"{build_tool} build -t judgoo/base-debian:v0.0.1 -f ./images/Dockerfile.debian.base ./images\n",
            "\n",
            f"sh {build_sh}\n",
        ]
    )

os.chmod(build_sh, 0o0777)
os.chmod(build_all, 0o0777)
