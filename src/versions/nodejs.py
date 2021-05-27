from src.helper.alpine_base import AlpineBaseDockerFile

BASE_IMAGE = "node:14-alpine3.13"

nodejs = AlpineBaseDockerFile("nodejs14", base_img=BASE_IMAGE)
nodejs.add_judger()

ts = AlpineBaseDockerFile(
    "typescript", base_img=BASE_IMAGE, build_args="--shm-size 512M"
)
ts.RUN = "YARN_CACHE_FOLDER=/dev/shm/yarn_cache yarn global add esbuild"
ts.add_judger()

ALL_IMAGES = [nodejs, ts]
