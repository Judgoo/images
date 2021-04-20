gen:
	python3 generate.py
clean:
	sudo docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs sudo docker rmi
	sudo docker images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs sudo docker rmi --force
