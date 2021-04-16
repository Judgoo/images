from .helper import AlpineBaseDockerFile

d = AlpineBaseDockerFile("ocaml")
d.RUN = "apk add --no-cache binutils ocaml --repository http://dl-cdn.alpinelinux.org/alpine/edge/community"

ALL_IMAGES = [d]
