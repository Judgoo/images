from .helper.base import DockerFile

d = DockerFile("nasm")
d.add_packages("binutils", "nasm")


ALL_IMAGES = [d]
