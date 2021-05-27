from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("swift5.3.3", "swift:5.3.3-focal")
d.add_judger()
d.ENV = "PATH $PATH:/usr/lib/"

ALL_IMAGES = [d]
