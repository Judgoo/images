from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("ruby")
d.add_packages("ruby")
d.add_judger()

ALL_IMAGES = [d]
