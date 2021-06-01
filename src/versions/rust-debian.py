from src import languages, recipes
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("rust1.51", "rust:1.51-slim-buster")
d.add_judger()

d._version = {
    "id": "rust1.51",
    "name": "Rust 1.51.0",
    "recipe": recipes.Rustc,
    "language": languages.Rust,
}


ALL_IMAGES = [d]
