from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("php7")
d.add_packages("php")
d.add_judger()

d._lang = languages.PHP
d._version = {
    "id": "php7",
    "name": "PHP 7.4.15",
    "recipe": recipes.PHP,
}


ALL_IMAGES = [d]
