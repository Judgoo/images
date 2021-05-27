from src.languages import Rust
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("rust1.51", "rust:1.51-slim-buster")
d.add_judger()

d._lang = Rust
d._recipe = {
    "build": ["rustc -o {output} {filename}"],
    "run": "./{output}",
}


ALL_IMAGES = [d]
