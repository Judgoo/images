from src.languages import Lua
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("lua")
d.add_packages("lua")
d.add_judger()

d._lang = Lua
d._recipe = {
    "build": [],
    "run": "lua {filename}",
}


ALL_IMAGES = [d]
