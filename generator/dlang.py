from .helper.base import DockerFile

d = DockerFile("dlang2")
d.add_packages("dmd", "gcc", "musl-dev")


ALL_IMAGES = [d]
