from src.image_wrapper import AlpineImageWrapper

d = AlpineImageWrapper("golang", "golang:1.16.3-alpine3.13")
d.add_judger()

ALL_IMAGES = [d]
