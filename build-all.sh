#!/bin/sh

podman build -t judgoo/base:v1 -f ./images/Dockerfile.base

python3 generate.py

sh build-images.sh
