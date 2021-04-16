from .helper import DebianBaseDockerFile

d = DebianBaseDockerFile("openjdk11", "adoptopenjdk/openjdk11:debianslim-slim")
d.add_judger()

ALL_IMAGES = [d]
