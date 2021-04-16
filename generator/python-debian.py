from .helper import DebianBaseDockerFile


py39 = DebianBaseDockerFile("python3.9", base_img="python:3.9-slim-buster")
py39.add_judger()

py39_w = DebianBaseDockerFile("python3.9w", base_img=py39)
py39_w.ARG = "PIP_NO_CACHE_DIR=1"
py39_w.RUN = "pip install --no-cache numpy pandas"

ALL_IMAGES = [py39, py39_w]
