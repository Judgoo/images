from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("php7")
d.add_packages("php")
d.add_judger()

ALL_IMAGES = [d]
