from src.languages import PHP
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("php7")
d.add_packages("php")
d.add_judger()

d._lang = PHP
d._recipe = {
    "build": [],
    "run": "php {filename}",
}


ALL_IMAGES = [d]
