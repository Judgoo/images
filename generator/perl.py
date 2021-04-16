from .helper import AlpineBaseDockerFile

d = AlpineBaseDockerFile("ruby")
d.add_packages("ruby")

ALL_IMAGES = [d]
