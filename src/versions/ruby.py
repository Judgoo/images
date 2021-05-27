from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("perl")
d.add_packages("perl")
d.add_judger()

ALL_IMAGES = [d]
