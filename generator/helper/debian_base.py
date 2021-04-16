from .base import BaseDockerFile


class DebianBaseDockerFile(BaseDockerFile):
    OS = "debian"

    def add_packages(self, *packages):
        self.RUN = f"""
RUN apt-get update && apt-get install -y {' '.join(packages)} \\
&& rm -rf /var/lib/apt/lists/*
"""
