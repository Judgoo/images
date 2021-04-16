from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("nasm")
d.add_packages("binutils", "nasm")


ALL_IMAGES = [d]
