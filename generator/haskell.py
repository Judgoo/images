from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("haskell")
d.add_packages("ghc")

ALL_IMAGES = [d]
