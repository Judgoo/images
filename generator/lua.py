from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("lua")
d.add_packages("lua")
d.add_judger()

ALL_IMAGES = [d]
