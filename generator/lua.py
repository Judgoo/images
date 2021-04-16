from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("lua")
d.add_packages("lua")

ALL_IMAGES = [d]
