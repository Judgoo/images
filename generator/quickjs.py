from .helper.alpine_base import AlpineBaseDockerFile

qjs_builder = AlpineBaseDockerFile("builder", base_img="alpine:latest")
qjs_builder.RUN = "apk add --no-cache xz make g++"
qjs_builder.ENV = "VERSION=2021-03-27"
qjs_builder.ADD = "https://bellard.org/quickjs/quickjs-${VERSION}.tar.xz /tmp"
qjs_builder.RUN = """ cd /tmp \
  && tar xf quickjs-${VERSION}.tar.xz \
  && cd quickjs-${VERSION} \
  && (make || true) \
  && mkdir /out \
  && mv qjs qjsc qjscalc /out
"""

qjs = AlpineBaseDockerFile("quickjs-2021-03-27")
qjs.add_builder(qjs_builder, "build")

qjs.COPY = "--from=build /out /usr/local/bin/"

ALL_IMAGES = [qjs]
