from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("gplusplus")
d.add_packages("g++")

ALL_IMAGES = [d]
