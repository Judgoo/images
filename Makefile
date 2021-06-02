gen:
	python3 generate.py
clean_docker:
	docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs docker rmi
	docker images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs docker rmi --force
clean_podman:
	podman images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs podman rmi
	podman images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs podman rmi --force

build_docker: gen
	./docker-build-all.sh
push_docker:
	./docker-push-all.sh
build_podman: gen
	./podman-build-all.sh
push_podman:
	./podman-push-all.sh

podman: build_podman push_podman
	echo podman
