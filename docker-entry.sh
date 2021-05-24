sudo docker run --privileged --rm -v $(pwd)/testdata:/workspace -it --entrypoint /bin/sh judgoo/$1:v0.0.1
