from helper.base import DockerFile
from helper.constants import VERSION

d = DockerFile(name="judgoo/assembly:" + VERSION)
d.add_packages("binutils", "nasm")

d.generate_files()
