from .helper.base import DockerFile

d = DockerFile("haskell")
d.add_packages("ghc")

ALL_IMAGES = [d]
