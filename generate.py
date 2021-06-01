import os
from collections import defaultdict
from os import listdir, makedirs, path, remove
from os.path import isfile, join
from typing import Any, DefaultDict, Dict, List

from yaml import dump

from src.constants import JUDGOO_VERSION
from src.image_wrapper import ImageWrapper
from src.versions import *  # noqa: F401


_s = {k: v for k, v in globals().items() if hasattr(v, "ALL_IMAGES")}

all_images: List[ImageWrapper] = []

for k, v in _s.items():
    all_images.extend(v.ALL_IMAGES)

makedirs("./images", exist_ok=True)
makedirs("./profiles", exist_ok=True)

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
                f"{build_tool} build -t judgoo/vendor-quickjs:v0.0.1 -f ./vendor/Dockerfile.quickjs ./vendor\n",
                "\n",
                f"sh {build_sh}\n",
            ]
        )

    os.chmod(build_all, 0o0777)


gen("docker")
gen("podman")


def save_yml(filename, dict_):
    content = dump(
        dict(dict_),
        indent=2,
        explicit_start=True,
    )
    with open(path.join("./profiles", filename), "w") as f:
        f.write(content)


def generate_dependency_map(all_images: List[ImageWrapper]):
    map_lang2version: DefaultDict[str, List[str]] = defaultdict(list)
    version_name2recipe: Dict[str, Dict[str, Any]] = dict()

    for image in all_images:
        version = image._version_name
        versions = (
            image._version if isinstance(image._version, list) else [image._version]
        )

        for version in versions:
            recipe = version["recipe"]
            lang_info = version["language"].to_dict()
            _result: Dict[str, Any] = {
                "build": [i.format_map(lang_info) for i in recipe.build],
                "run": recipe.run.format_map(lang_info),
                "name": version["name"],
                "image": image.get_img_name(),
                **lang_info,
            }
            map_lang2version[version["language"].__name__].append(version["id"])
            version_name2recipe[version["id"]] = _result

    save_yml("languages.yml", map_lang2version)
    save_yml("versions.yml", version_name2recipe)


generate_dependency_map(all_images)
