from .base import BaseDockerFile


class AlpineBaseDockerFile(BaseDockerFile):
    BASE_IMG = "alpine:3.13"
    OS = "alpine"

    def add_packages(self, *packages):
        self.RUN = f"apk add --no-cache {' '.join(packages)}"
