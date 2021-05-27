from src.helper import AlpineBaseDockerFile

d = AlpineBaseDockerFile("perl")
d.add_packages("perl")
d.add_judger()

ALL_IMAGES = [d]
