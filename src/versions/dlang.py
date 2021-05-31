from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("dlang2")
d.add_packages("dmd", "gcc", "musl-dev")
d.add_judger()


d._version = {
    "id": "dlang2",
    "name": "DMD v2.095.0",
    "recipe": recipes.DLang,
    "language": languages.D,
}


ALL_IMAGES = [d]
