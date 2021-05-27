from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("lua")
d.add_packages("lua")
d.add_judger()

ALL_IMAGES = [d]
