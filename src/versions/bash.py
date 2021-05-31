from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("bash")
d.add_packages("bash")
d.add_judger()

d._version = {
    "id": "bash",
    "name": "Bash(5.1.0)",
    "recipe": recipes.Bash,
    "language": languages.Bash,
}

ALL_IMAGES = [d]
