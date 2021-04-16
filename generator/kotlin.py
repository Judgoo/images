from .helper.alpine_base import AlpineBaseDockerFile

BASE_IMAGE = "adoptopenjdk/openjdk8:jdk8u282-b08-alpine-slim"
COMPILER_URL = "https://github.com/JetBrains/kotlin/releases/download/v1.4.32/kotlin-compiler-1.4.32.zip"

kt = AlpineBaseDockerFile("kotlin1.42", BASE_IMAGE)
kt.add_judger()
kt.RUN = f"""apk add --no-cache bash && \\
    apk add --no-cache -t build-dependencies wget && \\
    cd /usr/lib && \\
    wget -q {COMPILER_URL} && \\
    unzip kotlin-compiler-*.zip && \\
    rm kotlin-compiler-*.zip && \\
    rm -f kotlinc/bin/*.bat && \\
    apk del --no-cache build-dependencies
"""

kt.ENV = "PATH $PATH:/usr/lib/kotlinc/bin"

ALL_IMAGES = [kt]
