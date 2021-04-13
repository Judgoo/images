from .helper.base import DockerFile

d = DockerFile("openjdk11", "adoptopenjdk/openjdk11:jdk-11.0.10_9-alpine")
d.add_judger()

ALL_IMAGES = [d]
