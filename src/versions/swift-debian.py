from src import recipes, languages
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("swift5.3.3", "swift:5.3.3-focal")
d.add_judger()
d.ENV = "PATH $PATH:/usr/lib/"

d._version = {
    "id": "swift",
    "name": "Swift 5.3.3",
    "recipe": recipes.Swiftc,
    "language":  languages.Swift
}


ALL_IMAGES = [d]
