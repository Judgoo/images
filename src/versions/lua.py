from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("lua")
d.add_packages("lua")
d.add_judger()

d._lang = languages.Lua
d._version = {
    "id": "lua",
    "name": "Lua 5.1.5",
    "recipe": recipes.Lua,
}


ALL_IMAGES = [d]
