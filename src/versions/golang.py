from src.helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("golang", "golang:1.16.3-alpine3.13")
d.add_judger()

ALL_IMAGES = [d]
