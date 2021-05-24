from .helper import DebianBaseDockerFile

d = DebianBaseDockerFile("gpp")
d.add_packages("g++")
d.add_judger()

ALL_IMAGES = [d]
