from src.languages import Ocaml
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("ocaml")
d.RUN = "apk add --no-cache binutils ocaml --repository http://dl-cdn.alpinelinux.org/alpine/edge/community"
d.add_judger()

d._lang = Ocaml
d._recipe = {
    "build": ["ocamlc -o {output} {filename}"],
    "run": "./{output}",
}


ALL_IMAGES = [d]
