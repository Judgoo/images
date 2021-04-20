# images

## 生成容器 Dockerfile

项目根目录下的 `generate.py` 负责生成 `images/Dockerfile.*` 和 `build-images.sh` 文件。

## 开始使用

### podman

使用 podman 打包容器。

## 例子

使用 gcc 容器的例子：

```sh
podman run --rm -v $(pwd)/testdata:/workspace judgoo/gpp:v0.0.1 -d ./c
# interactive
podman run --rm -v $(pwd)/testdata:/workspace -it --entrypoint /bin/bash judgoo/gpp:v0.0.1
```

以此类推，`testdata` 下有各种支持的语言的判题数据。

## 清除镜像

更新了 base 镜像的话可能需要先清除所有当前版本的其他镜像。

首先需要先删除所有容器。

```sh
podman images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs podman rmi --force
```

清空 `<none>` 容器：

```bash
podman images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs podman rmi
```

移除所有 storage 容器：

```bash
podman ps --all --storage | awk 'NR>1{ print $1 }' | xargs podman container rm --force
```
