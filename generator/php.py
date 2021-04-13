from .helper.base import DockerFile

d = DockerFile("php")
d.add_packages("php")

ALL_IMAGES = [d]
