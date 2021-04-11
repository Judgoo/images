import sys
import logging
from . import docker
from .constants import VERSION

logging.getLogger("").setLevel(logging.INFO)
logging.root.addHandler(logging.StreamHandler(sys.stdout))


class BaseDockerFile(docker.DockerFile):
    def __init__(self, name: str, base_img=None):
        if base_img is None:
            base_img = "judgoo/base:" + VERSION
        if not name.startswith("judgoo/"):
            name = f"judgoo/{name}"
        if ":" not in name:
            name = f"{name}:{VERSION}"
        kwargs = {"build_tool": "podman"}
        super().__init__(base_img, name, **kwargs)

    def generate_files(self, **kwargs):
        kwargs.pop("path", None)
        return super().generate_files(path="./images", **kwargs)

    def add_packages(self, *packages):
        self.RUN = f"apk add --no-cache {' '.join(packages)}"

    def add_judger(self):
        """放到生成的最后"""
        self.FROM = f"judgoo/base:{VERSION} as base_builder"
        x = self._instructions.pop()
        self._instructions.insert(0, x)

        self.COPY = "--from=base_builder /tool/ /tool/"
        self.ENV = 'PATH="/tool:${PATH}"'
        self.WORKDIR = "/workspace"
        self.ENTRYPOINT = ["Judger"]


DockerFile = BaseDockerFile
