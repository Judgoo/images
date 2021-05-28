from src import recipes, languages
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("rust1.51", "rust:1.51-slim-buster")
d.add_judger()

d._lang = languages.Rust
d._version = {
    "id": "rust1.51",
    "name": "Rust 1.51.0",
    "recipe": recipes.Rustc,
}


ALL_IMAGES = [d]
