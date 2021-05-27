from src.languages import Haskell
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("haskell")
d.add_packages("ghc")
d.add_judger()


d._lang = Haskell
d._recipe = {
    "build": [],
    "run": "runghc {filename}",
}


ALL_IMAGES = [d]
