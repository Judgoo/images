from .base import BaseDockerFile


class AlpineBaseDockerFile(BaseDockerFile):
    OS = "alpine"

    def add_packages(self, *packages):
        self.RUN = f"apk add --no-cache {' '.join(packages)}"
