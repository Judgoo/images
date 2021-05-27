from src.languages import D
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("dlang2")
d.add_packages("dmd", "gcc", "musl-dev")
d.add_judger()


d._lang = D
d._recipe = {
    "build": ["dmd -of={output} {filename}"],
    "run": "./{output}",
}


ALL_IMAGES = [d]
