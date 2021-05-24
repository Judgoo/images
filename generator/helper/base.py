import sys
import logging
from . import docker
from .constants import VERSION

logging.getLogger("").setLevel(logging.INFO)
logging.root.addHandler(logging.StreamHandler(sys.stdout))


class BaseDockerFile(docker.DockerFile):
    OS: str

    def __init__(self, name: str, base_img=None, **kwargs):
        self._default_base_img = f"judgoo/base-{self.OS}:{VERSION}"
        if base_img is None:
            base_img = self._default_base_img
        if not name.startswith("judgoo/"):
            name = f"judgoo/{name}"
        if ":" not in name:
            name = f"{name}:{VERSION}"
        kwargs = {"build_tool": "docker", **kwargs}
        super(BaseDockerFile, self).__init__(base_img, name, **kwargs)

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
