from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("golang", "golang:1.16.3-alpine3.13")
d.add_judger()

d._lang = languages.Go
d._version = {
    "id": "golang1.16",
    "name": "Go 1.16.3",
    "recipe": recipes.GoLang,
}

ALL_IMAGES = [d]
