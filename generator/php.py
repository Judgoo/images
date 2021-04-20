from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("php7")
d.add_packages("php")

ALL_IMAGES = [d]
