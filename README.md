# images

## 开始使用
### podman

使用 podman 打包容器。

## 例子

使用 gcc 容器的例子：

```sh
podman run --runtime=crun -v $(pwd)/testdata:/workspace judgoo/gcc:v1 -d ./c
# interactive
podman run --runtime=crun -v $(pwd)/testdata:/workspace -it --entrypoint /bin/ash  judgoo/gcc:v1
```

使用 python 容器的例子：

```sh
podman run --runtime=crun -v $(pwd)/testdata:/workspace judgoo/python3.9:v1 -d ./python
# interactive
podman run --runtime=crun -v $(pwd)/testdata:/workspace -it --entrypoint /bin/ash  judgoo/python3.9:v1
```
