from .helper.alpine_base import AlpineBaseDockerFile

d = AlpineBaseDockerFile("csharp")

d.RUN = """
apk add --no-cache mono --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \\
    apk add --no-cache --virtual=.build-dependencies ca-certificates && \\
    cert-sync /etc/ssl/certs/ca-certificates.crt && \\
    apk del --no-cache .build-dependencies
""".strip()

ALL_IMAGES = [d]
