from src import recipes, languages
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("gpp")
d.add_packages("g++")
d.add_judger()


d._lang = [languages.C, languages.Cpp]
d._version = [
    {
        "id": "gcc",
        "name": "GCC 8.3.0",
        "recipe": recipes.GCC,
    },
    {
        "id": "gpp",
        "name": "G++ 8.3.0",
        "recipe": recipes.GPP,
    },
]


ALL_IMAGES = [d]
