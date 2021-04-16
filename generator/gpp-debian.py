from .helper import DebianBaseDockerFile

d = DebianBaseDockerFile("gpp-debian")
d.add_packages("g++")

ALL_IMAGES = [d]
