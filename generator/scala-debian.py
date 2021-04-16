from .helper import DebianBaseDockerFile

BASE_IMAGE = "adoptopenjdk/openjdk8:debianslim-slim"
SCALA_VERSION = "2.13.5"
SCALA_HOME = "/usr/share/scala"

s = DebianBaseDockerFile("scala", BASE_IMAGE)
s.add_judger()
s.RUN = f"""apt-get update && apt-get install -y --no-install-recommends wget && \\
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


ALL_IMAGES = [s]
