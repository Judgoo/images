# images

## 生成容器 Dockerfile

项目根目录下的 `generate.py` 负责生成 `images/Dockerfile.*` 和 `build-images.sh` 文件。

## 开始使用
### podman

使用 podman 打包容器。

## 例子

使用 gcc 容器的例子：

```sh
podman run --runtime=crun --rm -v $(pwd)/testdata:/workspace judgoo/gcc:v1 -d ./c
# interactive
podman run --runtime=crun --rm -v $(pwd)/testdata:/workspace -it --entrypoint /bin/ash judgoo/gcc:v1
```

使用 python 容器的例子：

```sh
podman run --runtime=crun --rm -v $(pwd)/testdata:/workspace judgoo/python3.8-with-packages:v1 -d ./python
# interactive
podman run --runtime=crun --rm -v $(pwd)/testdata:/workspace -it --entrypoint /bin/ash judgoo/python3.8-with-packages:v1
```
