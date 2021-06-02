docker build -t judgoo/base-alpine:v0.0.2 -f ./base/Dockerfile.alpine.base ./base
docker build -t judgoo/base-debian:v0.0.2 -f ./base/Dockerfile.debian.base ./base
docker build -t judgoo/vendor-quickjs:v0.0.1 -f ./vendor/Dockerfile.quickjs ./vendor

sh ./docker-build-images.sh
