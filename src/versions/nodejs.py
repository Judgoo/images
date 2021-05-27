from src.languages import JavaScript, TypeScript
from src.image_wrapper import AlpineImageWrapper

BASE_IMAGE = "node:14-alpine3.13"

nodejs = AlpineImageWrapper("nodejs14", base_img=BASE_IMAGE)
nodejs.add_judger()
nodejs._lang = JavaScript
nodejs._recipe = {
    "build": [],
    "run": "node {filename}",
}

esbuild = AlpineImageWrapper(
    "esbuild", base_img=BASE_IMAGE, build_args="--shm-size 512M"
)
esbuild.RUN = "YARN_CACHE_FOLDER=/dev/shm/yarn_cache yarn global add esbuild"
esbuild.add_judger()
esbuild._lang = TypeScript
esbuild._recipe = {
    "build": ["esbuild {filename} --outfile={output} --platform=node --target=node14"],
    "run": "node {output}",
}


ALL_IMAGES = [nodejs, esbuild]
