from .helper.base import DockerFile

d = DockerFile("gplusplus")
d.add_packages("g++")

ALL_IMAGES = [d]
