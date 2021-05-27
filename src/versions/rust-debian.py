from src.helper import DebianBaseDockerFile

d = DebianBaseDockerFile("rust1.51", "rust:1.51-slim-buster")
d.add_judger()

ALL_IMAGES = [d]
