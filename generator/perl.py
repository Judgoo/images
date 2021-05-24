from .helper import AlpineBaseDockerFile

d = AlpineBaseDockerFile("ruby")
d.add_packages("ruby")
d.add_judger()

ALL_IMAGES = [d]
