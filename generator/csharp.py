from .helper.base import DockerFile

d = DockerFile("csharp")

d.RUN = """
apk add --no-cache mono --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \\
    apk add --no-cache --virtual=.build-dependencies ca-certificates && \\
    cert-sync /etc/ssl/certs/ca-certificates.crt && \\
    apk del .build-dependencies
""".strip()

ALL_IMAGES = [d]
