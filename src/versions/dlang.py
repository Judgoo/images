from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("dlang2")
d.add_packages("dmd", "gcc", "musl-dev")
d.add_judger()

ALL_IMAGES = [d]
