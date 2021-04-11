import os
from typing import List
from generator.helper.base import BaseDockerFile
from generator import *  # noqa: F401

_s = {k: v for k, v in globals().items() if hasattr(v, "ALL_IMAGES")}

all_images: List[BaseDockerFile] = []

for k, v in _s.items():
    all_images.extend(v.ALL_IMAGES)

build_sh = "./build-images.sh"
f = open(build_sh, "w+")

for image in all_images:
    image.generate_files()
    cmd = image.get_build_command()
    f.write(cmd)
    f.write("\n")
    f.flush()

f.close()

os.chmod(build_sh, 0o0777)
