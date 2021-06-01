from src import languages, recipes
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("gpp")
d.add_packages("g++")
d.add_judger()


d._version = [
    {
        "id": "gcc",
        "name": "GCC 8.3.0",
        "recipe": recipes.GCC,
        "language": languages.C,
    },
    {
        "id": "gpp",
        "name": "G++ 8.3.0",
        "recipe": recipes.GPP,
        "language": languages.Cpp,
    },
]


ALL_IMAGES = [d]
