from src import languages, recipes
from src.image_wrapper import AlpineImageWrapper

qjs_builder = AlpineImageWrapper("builder", base_img="alpine:latest")
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

qjs = AlpineImageWrapper("quickjs-2021-03-27")
qjs.add_builder("judgoo/vendor-quickjs:v0.0.1", "qjs_builder")

qjs.COPY = "--from=qjs_builder /out /usr/local/bin/"
qjs.add_judger()


qjs._version = {
    "id": "quickjs-2021-03-27",
    "name": "QuickJS 2021-03-27",
    "recipe": recipes.QJS,
    "language": languages.JavaScript,
}


ALL_IMAGES = [qjs]
