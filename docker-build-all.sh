sudo docker build -t judgoo/base-alpine:v0.0.2 -f ./base/Dockerfile.alpine.base ./base
sudo docker build -t judgoo/base-debian:v0.0.2 -f ./base/Dockerfile.debian.base ./base

sh ./docker-build-images.sh
