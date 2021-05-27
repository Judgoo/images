from src.languages import Assembly
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("nasm")

d._lang = Assembly
d._recipe = {
    "build": [
        "nasm -f elf64 -o a.o {filename}",
        "ld -o {output} a.o",
    ],
    "run": "./{output}",
}

d.add_packages("binutils", "nasm")
d.add_judger()

ALL_IMAGES = [d]
