from src.languages import Java
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("openjdk11", "adoptopenjdk/openjdk11:debianslim-slim")
d.add_judger()

d._lang = Java
d._recipe = {
    "build": ["javac {filename}"],
    "run": "java {filestem}",
}


ALL_IMAGES = [d]
