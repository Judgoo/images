from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("perl")
d.add_packages("perl")
d.add_judger()


d._version = {
    "id": "perl",
    "name": "Perl 5.32.0",
    "recipe": recipes.Perl,
    "language": languages.Perl,
}


ALL_IMAGES = [d]
