from src.languages import C, Cpp
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("gpp")
d.add_packages("g++")
d.add_judger()


d._lang = [C, Cpp]
d._recipe = [
    {
        "build": ["gcc -lm -w -O3 -std=gnu17 {filename} -o {output}"],
        "run": "./{output}",
    },
    {
        "build": ["g++ -lm -w -O3 -std=gnu++17 {filename} -o {output}"],
        "run": "./{output}",
    },
]


ALL_IMAGES = [d]
