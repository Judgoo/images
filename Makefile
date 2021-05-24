gen:
	python3 generate.py
clean_docker:
	sudo docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs sudo docker rmi
	sudo docker images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs sudo docker rmi --force
build_docker: gen
	./build-all-docker.sh
push_docker:
	./push-all-docker.sh
build_podman: gen
	./build-all-podman.sh
