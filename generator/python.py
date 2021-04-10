from .helper.base import DockerFile


py39 = DockerFile("python3.9", base_img="python:3.9.4-alpine3.13")

py39.RUN = "pip3 install numpy pandas"

py39.add_judger()
py39.generate_files()
