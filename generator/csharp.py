from .helper.debian_base import DebianBaseDockerFile

d = DebianBaseDockerFile("csharp", "mcr.microsoft.com/dotnet/sdk:5.0-buster-slim")
d.add_judger()

ALL_IMAGES = [d]
