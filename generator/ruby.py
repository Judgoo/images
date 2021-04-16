from .helper import AlpineBaseDockerFile

d = AlpineBaseDockerFile("perl")
d.add_packages("perl")

ALL_IMAGES = [d]
