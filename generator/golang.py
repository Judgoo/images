from .helper.base import DockerFile

d = DockerFile("golang", "golang:1.16.3-alpine3.13")
d.add_judger()

ALL_IMAGES = [d]
