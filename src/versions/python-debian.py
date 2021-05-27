from src.image_wrapper import DebianImageWrapper


py27 = DebianImageWrapper("python2.7", base_img="python:2.7.18-slim-buster")
py27.RUN = "pip install --no-cache numpy pandas"
py27.add_judger()

py39 = DebianImageWrapper("python3.9", base_img="python:3.9-slim-buster")
py39.RUN = "pip install --no-cache numpy pandas"
py39.add_judger()

ALL_IMAGES = [py27, py39]
