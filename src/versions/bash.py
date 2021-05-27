from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("bash")
d.add_packages("bash")
d.add_judger()

ALL_IMAGES = [d]
