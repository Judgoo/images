import os
from os import listdir, remove
from os.path import isfile, join
from typing import List

from generator import *  # noqa: F401
from generator.helper.base import BaseDockerFile

build_tool = "podman"

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

build_sh = "./build-images.sh"
build_all = "./build-all.sh"
f = open(build_sh, "w+")

for image in all_images:
    image.generate_files()
    f.write(image.get_build_command(build_tool=build_tool))
    f.write("\n")
    f.flush()

f.close()

with open(build_all, "w+") as f:
    f.writelines(
        [
            f"{build_tool} build -t judgoo/base-alpine:v0.0.1 -f ./images/Dockerfile.alpine.base .\n",
            f"{build_tool} build -t judgoo/base-debian:v0.0.1 -f ./images/Dockerfile.debian.base .\n",
            "\n",
            "sh build-images.sh\n",
        ]
    )

os.chmod(build_sh, 0o0777)
