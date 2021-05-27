from src.languages import Ruby
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("ruby")
d.add_packages("ruby")
d.add_judger()

d._lang = Ruby
d._recipe = {
    "build": [],
    "run": "ruby {filename}",
}


ALL_IMAGES = [d]
