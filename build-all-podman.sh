podman build -t judgoo/base-alpine:v0.0.1 -f ./images/Dockerfile.alpine.base ./images
podman build -t judgoo/base-debian:v0.0.1 -f ./images/Dockerfile.debian.base ./images

sh ./build-images-podman.sh
