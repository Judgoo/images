from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("ocaml")
d.RUN = "apk add --no-cache binutils ocaml --repository http://dl-cdn.alpinelinux.org/alpine/edge/community"
d.add_judger()

ALL_IMAGES = [d]
