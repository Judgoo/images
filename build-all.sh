podman build -t judgoo/base-alpine:v0.0.1 -f ./images/Dockerfile.alpine.base .
podman build -t judgoo/base-debian:v0.0.1 -f ./images/Dockerfile.debian.base .

sh build-images.sh
