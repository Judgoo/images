from typing import List


class Recipe:
    build: List[str]
    run: str


class NASM(Recipe):
    build = [
        "nasm -f elf64 -o a.o {filename}",
        "ld -o {output} a.o",
    ]
    run = "./{output}"


class Bash(Recipe):
    build = []
    run = "bash {filename}"


class CSharp(Recipe):
    build = ["mcs -out:{output} {filename}"]
    run = "mono {output}"


class DLang(Recipe):
    build = ["dmd -of={output} {filename}"]
    run = "./{output}"


class GoLang(Recipe):
    build = ["go build -o {output} {filename}"]
    run = "./{output}"


class GCC(Recipe):
    build = ["gcc -lm -w -O3 -std=gnu17 {filename} -o {output}"]
    run = "./{output}"


class GPP(Recipe):
    build = ["g++ -lm -w -O3 -std=gnu++17 {filename} -o {output}"]
    run = "./{output}"


class GHC(Recipe):
    build = []
    run = "runghc {filename}"


class Javac(Recipe):
    build = ["javac {filename}"]
    run = "java {filestem}"


class Julia(Recipe):
    build = []
    run = "julia {filename}"


class Lua(Recipe):
    build = []
    run = "lua {filename}"


class Nodejs(Recipe):
    build = []
    run = "node {filename}"


class EsBuild(Recipe):
    build = ["esbuild {filename} --outfile={output} --platform=node --target=node14"]
    run = "node {output}"


class Ocamlc(Recipe):
    build = ["ocamlc -o {output} {filename}"]
    run = "./{output}"


class Scalac(Recipe):
    build = ["scalac {filename}"]
    run = "scala {output}"


class Kotlinc(Recipe):
    build = ["kotlinc {filename}"]
    run = "kotlin {filestem}Kt"


class Perl(Recipe):
    build = []
    run = "perl {filename}"


class PHP(Recipe):
    build = []
    run = "php {filename}"


class Python(Recipe):
    build = []
    run = "python {filename}"


class Ruby(Recipe):
    build = []
    run = "ruby {filename}"


class QJS(Recipe):
    build = []
    run = "qjs {filename}"


class Rustc(Recipe):
    build = ["rustc -o {output} {filename}"]
    run = "./{output}"


class Swiftc(Recipe):
    build = ["swiftc -o {output} {filename}"]
    run = "./{output}"
