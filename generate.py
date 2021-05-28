import os
from collections import defaultdict
from os import listdir, makedirs, remove
from os.path import isfile, join
from typing import Any, DefaultDict, Dict, List

from yaml import dump

from src.constants import JUDGOO_VERSION
from src.image_wrapper import ImageWrapper
from src.versions import *  # noqa: F401


def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


_s = {k: v for k, v in globals().items() if hasattr(v, "ALL_IMAGES")}

all_images: List[ImageWrapper] = []

for k, v in _s.items():
    all_images.extend(v.ALL_IMAGES)

makedirs("./images", exist_ok=True)

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
        f.write(f"{build_tool} push judgoo/base-alpine:{JUDGOO_VERSION}\n")
        f.write(f"{build_tool} push judgoo/base-debian:{JUDGOO_VERSION}\n")
    os.chmod(push_all, 0o0777)

    if build_tool == "docker":
        build_tool = "sudo docker"

    with open(build_all, "w+") as f:
        f.writelines(
            [
                f"{build_tool} build -t judgoo/base-alpine:{JUDGOO_VERSION} -f ./base/Dockerfile.alpine.base ./base\n",
                f"{build_tool} build -t judgoo/base-debian:{JUDGOO_VERSION} -f ./base/Dockerfile.debian.base ./base\n",
                "\n",
                f"sh {build_sh}\n",
            ]
        )

    os.chmod(build_all, 0o0777)


gen("docker")
gen("podman")


def generate_dependency_map(all_images: List[ImageWrapper]):
    map_lang2version: DefaultDict[str, List[str]] = defaultdict(list)
    version_name2recipe: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)
    for image in all_images:
        print(image._image_name)
        version = image._version_name
        langs = image._lang if isinstance(image._lang, list) else [image._lang]
        versions = (
            image._version if isinstance(image._version, list) else [image._version]
        )

        if len(langs) != len(versions):
            print(f"{image._image_name} langs and versions length not equal")
            return
        for lang, version in zip(langs, versions):
            recipe = version["recipe"]
            _result: Dict[str, Any] = {
                "build": [i.format_map(lang.to_dict()) for i in recipe.build],
                "run": recipe.run.format_map(lang.to_dict()),
                "name": version["name"],
                "image": image.get_img_name(),
                **lang.to_dict(),
            }
            map_lang2version[lang.__name__].append(version["id"])
            version_name2recipe[version["id"]].append(_result)

    write_file("languages.yml", dump(dict(map_lang2version)))
    write_file(
        "versions.yml",
        dump(
            dict(version_name2recipe),
            indent=2,
            explicit_start=True,
        ),
    )


generate_dependency_map(all_images)
