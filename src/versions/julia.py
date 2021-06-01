from src import languages, recipes
from src.image_wrapper import AlpineImageWrapper

BASE_IMAGE = "julia:1.6.0-alpine3.13"

julia = AlpineImageWrapper("julia1.6", base_img=BASE_IMAGE)
julia.add_judger()

julia._version = {
    "id": "julia1.6",
    "name": "Julia 1.6.0",
    "recipe": recipes.Julia,
    "language":  languages.Julia
}


ALL_IMAGES = [julia]
