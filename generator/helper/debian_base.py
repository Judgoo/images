from .base import BaseDockerFile


class DebianBaseDockerFile(BaseDockerFile):
    OS = "debian"

    def add_packages(self, *packages):
        self.RUN = f"""apt-get update && \\
apt-get install -y --no-install-recommends {' '.join(packages)} && \\
rm -rf /var/lib/apt/lists/*"""
