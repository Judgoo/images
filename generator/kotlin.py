from .helper import DebianBaseDockerFile

BASE_IMAGE = "adoptopenjdk/openjdk8:debianslim-slim"
COMPILER_URL = "https://github.com/JetBrains/kotlin/releases/download/v1.4.32/kotlin-compiler-1.4.32.zip"

kt = DebianBaseDockerFile("kotlin1.42", BASE_IMAGE)
kt.add_judger()
kt.RUN = f"""apt-get update && apt-get install -y --no-install-recommends wget unzip && \\
    rm -rf /var/lib/apt/lists/* && \\
    cd /usr/lib && \\
    wget -q {COMPILER_URL} && \\
    unzip kotlin-compiler-*.zip && \\
    apt-get remove -y wget unzip && \\
    apt-get autoremove -y && \\
    apt-get autoclean -y && \\
    rm kotlin-compiler-*.zip && \\
    rm -f kotlinc/bin/*.bat
"""

kt.ENV = "PATH $PATH:/usr/lib/kotlinc/bin"

ALL_IMAGES = [kt]
