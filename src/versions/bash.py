from src.languages import Bash
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("bash")
d.add_packages("bash")
d.add_judger()

d._lang = Bash
d._recipe = {
    "build": [],
    "run": "bash {filename}",
}

ALL_IMAGES = [d]
