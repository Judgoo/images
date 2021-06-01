from typing import List, Type, TypedDict, Union

from .constants import JUDGOO_VERSION
from .helper import docker
from .languages import Language
from .recipes import Recipe


class Version(TypedDict):
    id: str
    name: str
    recipe: Type["Recipe"]
    language: Type["Language"]


class ImageWrapper(docker.DockerFile):
    BASE_IMG: str
    OS: str
    _is_add_judger: bool

    _version: Union[Version, List[Version]]

    def __init__(self, name: str, base_img=None, **kwargs):
        self._default_base_img = f"judgoo/base-{self.OS}:{JUDGOO_VERSION}"
        self._is_add_judger = False
        if base_img is None:
            base_img = self.BASE_IMG
        self._version_name = name
        use_judgoo = kwargs.get("use_judgoo")
        if use_judgoo:
            base_img = self._default_base_img
        if not name.startswith("judgoo/"):
            name = f"judgoo/{name}"
        if ":" not in name:
            name = f"{name}:{JUDGOO_VERSION}"
        kwargs = {"build_tool": "docker", **kwargs}
        super(ImageWrapper, self).__init__(base_img, name, **kwargs)

    def generate_files(self, **kwargs):
        kwargs.pop("path", None)
        return super().generate_files(path="./images", **kwargs)

    def add_packages(self, *packages):
        self.RUN = f"apk add --no-cache {' '.join(packages)}"

    def add_judger(self):
        self.add_front_from(f"{self._default_base_img} as base_builder")

        self.COPY = "--from=base_builder /tool/ /tool/"
        self.ENV = 'PATH="/tool:${PATH}"'
        self.WORKDIR = "/workspace"
        self.ENTRYPOINT = ["Judger"]
        self._is_add_judger = True


class AlpineImageWrapper(ImageWrapper):
    BASE_IMG = "alpine:3.13"
    OS = "alpine"

    def add_packages(self, *packages):
        self.RUN = f"apk add --no-cache {' '.join(packages)}"


class DebianImageWrapper(ImageWrapper):
    BASE_IMG = "debian:buster-slim"
    OS = "debian"

    def add_packages(self, *packages):
        self.RUN = f"""apt-get update && \\
apt-get install -y --no-install-recommends {' '.join(packages)} && \\
rm -rf /var/lib/apt/lists/*"""
