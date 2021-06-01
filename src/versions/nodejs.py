from src import languages, recipes
from src.image_wrapper import AlpineImageWrapper

BASE_IMAGE = "node:14-alpine3.13"

nodejs = AlpineImageWrapper("nodejs14", base_img=BASE_IMAGE)
nodejs.add_judger()

nodejs._version = {
    "id": "nodejs14",
    "name": "Node.js 14.16.1",
    "recipe": recipes.Nodejs,
    "language": languages.JavaScript,
}

esbuild = AlpineImageWrapper(
    "esbuild", base_img=BASE_IMAGE, build_args="--shm-size 512M"
)
esbuild.RUN = "YARN_CACHE_FOLDER=/dev/shm/yarn_cache yarn global add esbuild"
esbuild.add_judger()
esbuild._version = {
    "id": "esbuild",
    "name": "esbuild 0.11.14",
    "recipe": recipes.EsBuild,
    "language": languages.TypeScript,
}


ALL_IMAGES = [nodejs, esbuild]
