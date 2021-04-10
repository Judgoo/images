# images

## 开始使用
### podman

使用 podman 打包容器。

## 例子

提供了一个使用 gcc 容器的例子：

```sh
podman run --runtime=crun -v $(pwd)/testdata:/workspace judgoo/gcc:v1
# interactive
podman run --runtime=crun -v $(pwd)/testdata:/workspace -it --entrypoint /bin/ash  judgoo/gcc:v1
```
