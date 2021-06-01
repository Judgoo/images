from src import languages, recipes
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("csharp")

d.RUN = """
apk add --no-cache mono --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \\
    apk add --no-cache --virtual=.build-dependencies ca-certificates && \\
    cert-sync /etc/ssl/certs/ca-certificates.crt && \\
    apk del --no-cache .build-dependencies
""".strip()
d.add_judger()

d._version = {
    "id": "csharp",
    "name": "Mono 6.12.0.122",
    "recipe": recipes.CSharp,
    "language": languages.CSharp,
}


ALL_IMAGES = [d]
