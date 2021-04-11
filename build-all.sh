#!/bin/sh

podman build -t judgoo/base:v1 -f ./images/Dockerfile.base

python3 generate.py

# podman build -t judgoo/assembly:v1 -f ./images/Dockerfile.assembly
# podman build -t judgoo/bash:v1 -f ./images/Dockerfile.bash
# podman build -t judgoo/csharp:v1 -f ./images/Dockerfile.csharp
# podman build -t judgoo/gcc:v1 -f ./images/Dockerfile.gcc
# podman build -t judgoo/python3.9:v1 -f ./images/Dockerfile.python3.9
