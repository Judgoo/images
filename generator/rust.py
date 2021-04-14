from .helper.base import DockerFile

d = DockerFile("rust", "rust:1.51.0-alpine3.13")
d.add_judger()

ALL_IMAGES = [d]
