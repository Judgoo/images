from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("bash")
d.add_packages("bash")

ALL_IMAGES = [d]
