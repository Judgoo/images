from .helper.base import DockerFile

d = DockerFile("assembly")
d.add_packages("binutils", "nasm")


ALL_IMAGES = [d]
