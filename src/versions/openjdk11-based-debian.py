from src import recipes, languages
from src.image_wrapper import DebianImageWrapper

d = DebianImageWrapper("openjdk11", "adoptopenjdk/openjdk11:debianslim-slim")
d.add_judger()

d._version = {
    "id": "openjdk11",
    "name": "OpenJDK 11.0.10",
    "recipe": recipes.Javac,
    "language": languages.Java,
}


ALL_IMAGES = [d]
