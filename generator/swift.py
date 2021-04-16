from .helper import DebianBaseDockerFile

d = DebianBaseDockerFile("swift", "swift:5.3.3-focal")
d.add_judger()
d.ENV = "PATH $PATH:/usr/lib/"

ALL_IMAGES = [d]
