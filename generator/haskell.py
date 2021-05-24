from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("haskell")
d.add_packages("ghc")
d.add_judger()

ALL_IMAGES = [d]
