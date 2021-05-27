from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("haskell")
d.add_packages("ghc")
d.add_judger()

ALL_IMAGES = [d]
