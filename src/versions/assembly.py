from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("nasm")
d.add_packages("binutils", "nasm")
d.add_judger()

ALL_IMAGES = [d]
