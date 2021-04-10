from helper.base import DockerFile
from helper.constants import VERSION

d = DockerFile(name="judgoo/gcc:" + VERSION)
d.add_packages("gcc", "musl-dev")

d.generate_files()
