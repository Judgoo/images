from .helper.base import DockerFile

d = DockerFile("lua")
d.add_packages("lua")

ALL_IMAGES = [d]
