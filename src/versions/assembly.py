from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("nasm")
d.add_packages("binutils", "nasm")
d.add_judger()

d._lang = languages.Assembly
d._version = {
    "id": "nasm",
    "name": "NASM 2.15.05",
    "recipe": recipes.NASM,
}

ALL_IMAGES = [d]
