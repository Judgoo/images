from src import recipes, languages
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("ocaml")
d.RUN = "apk add --no-cache binutils ocaml --repository http://dl-cdn.alpinelinux.org/alpine/edge/community"
d.add_judger()

d._version = {
    "id": "ocaml",
    "name": "Ocaml 4.12.0",
    "recipe": recipes.Ocamlc,
    "language": languages.Ocaml,
}


ALL_IMAGES = [d]
