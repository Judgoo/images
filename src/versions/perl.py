from src.languages import Perl
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("perl")
d.add_packages("perl")
d.add_judger()


d._lang = Perl
d._recipe = {
    "build": [],
    "run": "perl {filename}",
}




ALL_IMAGES = [d]
