from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("php")
d.add_packages("php")

ALL_IMAGES = [d]
