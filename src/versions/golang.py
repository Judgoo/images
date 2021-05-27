from src.languages import Go
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("golang", "golang:1.16.3-alpine3.13")
d.add_judger()

d._lang = Go
d._recipe = {
    "build": ["go build -o {output} {filename}"],
    "run": "./{output}",
}

ALL_IMAGES = [d]
