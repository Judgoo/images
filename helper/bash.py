from helper.base import DockerFile
from helper.constants import VERSION

d = DockerFile(name="judgoo/bash:" + VERSION)
d.add_packages("bash")

d.generate_files()
