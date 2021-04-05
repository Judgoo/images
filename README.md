# images

## 开始使用
### podman

使用 podman 打包容器。

## 例子
### gcc

gcc 的容器提供了一个判题例子：

```sh
cd gcc
podman run --runtime=crun -v $(pwd)/data:/workspace judgoo/gcc:v1
```
