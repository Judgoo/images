# images

## 生成容器 Dockerfile

项目根目录下的 `generate.py` 负责生成 `images/Dockerfile.*` 和 `*.sh` 文件。

## 开始使用

### docker

使用 docker 打包容器。

## 例子

使用 gcc 容器的例子：

```sh
docker run --rm -v $(pwd)/testdata:/workspace judgoo/gpp:v0.0.1 -d ./c
# interactive
docker run --rm -v $(pwd)/testdata:/workspace -it --entrypoint /bin/bash judgoo/gpp:v0.0.1
```

在容器内部可以打开 c，cpp 这些文件夹，执行 `Judger`， `runner xxx` 等命令试一下。

以此类推，`testdata` 下有各种支持的语言的判题数据。

## 清除镜像

更新了 base 镜像的话可能需要先清除所有当前版本的其他镜像。

首先需要先删除所有容器。

```sh
docker images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs docker rmi --force
podman images --no-trunc | grep 'judgoo' | awk '{ print $3 }' | xargs podman rmi --force
```

清空 `<none>` 容器：

```bash
docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs docker rmi
podman images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs podman rmi
```

## 推送镜像到 Docker Hub

docker 正常登录推送即可。

podman 需要指定登录地址为 docker.io：

```bash
podman login docker.io
```

## 架构

每种 Language 就是一种语言，比如说 Javascript、Python。

每个 Version 就是同一个 Language 的不同版本，比如说 JavaScript 有 Nodejs14, Nodejs16, QuickJS 等。

每种 Recipe 就是指某种运行代码的方式，类声明和例子如下。

```python

class Recipe:
    build: List[str]
    run: str


class NASM(Recipe):
    build = [
        "nasm -f elf64 -o a.o {filename}",
        "ld -o {output} a.o",
    ]
    run = "./{output}"
```

每个 Version 有全局唯一的 ID 值，与 Recipe 是组合的关系。


来个例子：
JavaScript 语言有三种 Version：Nodejs14、Nodejs16 和 QuickJS。 Version 内容如下：

```python
nodejs14._version = {
    "id": "nodejs14",
    "name": "Node.js 14.16.1",
    "recipe": recipes.Nodejs,
    "language": languages.JavaScript,
}
nodejs16._version = {
    "id": "nodejs14",
    "name": "Node.js 16.2.0",
    "recipe": recipes.Nodejs,
    "language": languages.JavaScript,
}
qjs._version = {
    "id": "quickjs-2021-03-27",
    "name": "QuickJS 2021-03-27",
    "recipe": recipes.QJS,
    "language": languages.JavaScript,
}
```
Nodejs14、Nodejs16 都共享一个叫 Nodejs 的 Recipe，而同为 Nodejs 语言的 QuickJS 却会使用 qjs 这个 Recipe。

```python
class QJS(Recipe):
    build = []
    run = "qjs {filename}"

class Nodejs(Recipe):
    build = []
    run = "node {filename}"
```
