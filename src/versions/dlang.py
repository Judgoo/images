from src.helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("dlang2")
d.add_packages("dmd", "gcc", "musl-dev")
d.add_judger()

ALL_IMAGES = [d]
