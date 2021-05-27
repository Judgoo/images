from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("rust1.51", "rust:1.51-slim-buster")
d.add_judger()

ALL_IMAGES = [d]
