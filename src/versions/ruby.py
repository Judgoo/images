from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("ruby")
d.add_packages("ruby")
d.add_judger()

d._lang = languages.Ruby
d._version = {
    "id": "ruby",
    "name": "Ruby 2.7.3",
    "recipe": recipes.Ruby,
}


ALL_IMAGES = [d]
