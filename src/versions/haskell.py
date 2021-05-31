from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("haskell")
d.add_packages("ghc")
d.add_judger()


d._version = {
    "id": "haskell",
    "name": "GHC 8.8.4",
    "recipe": recipes.GHC,
    "language": languages.Haskell,
}


ALL_IMAGES = [d]
