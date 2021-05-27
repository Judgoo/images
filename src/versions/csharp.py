from src.languages import CSharp
from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("csharp")

d.RUN = """
apk add --no-cache mono --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \\
    apk add --no-cache --virtual=.build-dependencies ca-certificates && \\
    cert-sync /etc/ssl/certs/ca-certificates.crt && \\
    apk del --no-cache .build-dependencies
""".strip()
d.add_judger()

d._lang = CSharp
d._recipe = {
    "build": ["mcs -out:{output} {filename}"],
    "run": "mono {output}",
}


ALL_IMAGES = [d]
