from src.helper import DebianBaseDockerFile

BASE_IMAGE = "adoptopenjdk/openjdk8:debianslim-slim"

SCALA_VERSION = "2.13.5"
SCALA_HOME = "/usr/share/scala"

scala = DebianBaseDockerFile(f"scala{SCALA_VERSION}", BASE_IMAGE)
scala.add_judger()
scala.RUN = f"""apt-get update && apt-get install -y --no-install-recommends wget && \\
    rm -rf /var/lib/apt/lists/* && \\
    cd "/tmp" && \\
    wget "https://downloads.typesafe.com/scala/{SCALA_VERSION}/scala-{SCALA_VERSION}.tgz" && \\
    tar xzf "scala-{SCALA_VERSION}.tgz" && \\
    mkdir "{SCALA_HOME}" && \\
    rm "/tmp/scala-{SCALA_VERSION}/bin/"*.bat && \\
    mv "/tmp/scala-{SCALA_VERSION}/bin" "/tmp/scala-{SCALA_VERSION}/lib" "{SCALA_HOME}" && \\
    ln -s "{SCALA_HOME}/bin/"* "/usr/bin/" && \\
    apt-get remove -y wget && \\
    apt-get autoremove -y && \\
    apt-get autoclean -y && \\
    rm -rf "/tmp/"*
"""

KOTLIN_VERSION = "1.4.32"
COMPILER_URL = f"https://github.com/JetBrains/kotlin/releases/download/v{KOTLIN_VERSION}/kotlin-compiler-{KOTLIN_VERSION}.zip"

kt = DebianBaseDockerFile(f"kotlin{KOTLIN_VERSION}", BASE_IMAGE)
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


ALL_IMAGES = [scala, kt]
