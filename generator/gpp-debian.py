from .helper import DebianBaseDockerFile

d = DebianBaseDockerFile("gpp")
d.add_packages("g++")

ALL_IMAGES = [d]
