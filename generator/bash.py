from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("bash")
d.add_packages("bash")
d.add_judger()

ALL_IMAGES = [d]
