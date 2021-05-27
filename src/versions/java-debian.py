from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("openjdk11", "adoptopenjdk/openjdk11:debianslim-slim")
d.add_judger()

ALL_IMAGES = [d]
