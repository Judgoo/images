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
    if f.endswith(".base"):
        continue
    p = join("./images", f)
    if isfile(p):
        remove(p)

build_sh = "./build-images.sh"
f = open(build_sh, "w+")

for image in all_images:
    image.generate_files()
    f.write(image.get_build_command())
    f.write("\n")
    f.flush()

f.close()

os.chmod(build_sh, 0o0777)
