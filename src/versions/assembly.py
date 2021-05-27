from src.helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("nasm")
d.add_packages("binutils", "nasm")
d.add_judger()


ALL_IMAGES = [d]
