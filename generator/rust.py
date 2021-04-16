from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("rust1.51", "rust:1.51.0-alpine3.13")
d.add_judger()

ALL_IMAGES = [d]
