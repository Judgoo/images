from .helper.base import DockerFile


py39 = DockerFile("python3.9", base_img="python:3.9-alpine3.13")
py39.add_judger()

py38_w = DockerFile("python3-with-packages")
py38_w.add_packages("python3 py3-pandas py3-numpy")

ALL_IMAGES = [py39, py38_w]
