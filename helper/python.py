from helper.base import DockerFile
from helper.constants import VERSION

d = DockerFile(name="judgoo/python:" + VERSION, base_img="python:3.9.4-alpine3.13")
d.add_judger()
d.generate_files()
