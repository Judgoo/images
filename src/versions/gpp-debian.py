from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("gpp")
d.add_packages("g++")
d.add_judger()

ALL_IMAGES = [d]
