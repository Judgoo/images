from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("dlang2")
d.add_packages("dmd", "gcc", "musl-dev")


ALL_IMAGES = [d]
