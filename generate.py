import os
from os import listdir, remove
from os.path import isfile, join
from typing import List

from generator import *  # noqa: F401
from generator.helper.base import BaseDockerFile
from generator.helper.constants import VERSION

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


def gen(build_tool):
    build_sh = f"./{build_tool}-build-images.sh"
    build_all = f"./{build_tool}-build-all.sh"
    push_all = f"./{build_tool}-push-all.sh"

    print(f"generate {build_tool} related..")
    with open(build_sh, "w+") as f:
        for image in all_images:
            f.write(image.get_build_command(build_tool=build_tool))
            f.write("\n")
            f.flush()
    os.chmod(build_sh, 0o0777)

    with open(push_all, "w+") as f:
        for image in all_images:
            if not image._is_add_judger:
                image.add_judger()
            f.write(f"{build_tool} push {image.get_img_name()}\n")
            f.flush()
        f.write(f"{build_tool} push judgoo/base-alpine:{VERSION}\n")
        f.write(f"{build_tool} push judgoo/base-debian:{VERSION}\n")
    os.chmod(push_all, 0o0777)

    if build_tool == "docker":
        build_tool = "sudo docker"

    with open(build_all, "w+") as f:
        f.writelines(
            [
                f"{build_tool} build -t judgoo/base-alpine:{VERSION} -f ./base/Dockerfile.alpine.base ./base\n",
                f"{build_tool} build -t judgoo/base-debian:{VERSION} -f ./base/Dockerfile.debian.base ./base\n",
                "\n",
                f"sh {build_sh}\n",
            ]
        )

    os.chmod(build_all, 0o0777)


gen("docker")
gen("podman")
