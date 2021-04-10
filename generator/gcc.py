from .helper.base import DockerFile

d = DockerFile("gcc")
d.add_packages("gcc", "musl-dev")

d.generate_files()
