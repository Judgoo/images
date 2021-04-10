from .helper.base import DockerFile

d = DockerFile("bash")
d.add_packages("bash")

d.generate_files()
