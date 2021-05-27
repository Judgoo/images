from dataclasses import dataclass
from src.image_wrapper import Recipe
from typing import Optional


@dataclass(init=False)
class Language:
    filestem: str = "main"
    ext: str = "txt"
    output: Optional[str]
    mco: bool = False
    recipe: Optional[Recipe]


class Assembly(Language):
    ext = "asm"


class Bash(Language):
    ext = "bash"


class C(Language):
    ext = "c"


class Cpp(Language):
    ext = "cpp"


class CSharp(Language):
    ext = "cs"
    output = "a.exe"


class D(Language):
    ext = "d"


class Go(Language):
    ext = "go"


class Haskell(Language):
    ext = "hs"


class Java(Language):
    ext = "java"
    mco = True
    filestem = "Main"


class JavaScript(Language):
    ext = "js"
    mco = True


class Julia(Language):
    ext = "jl"


class Kotlin(Language):
    ext = "kt"
    filestem = "Main"


class Lua(Language):
    ext = "lua"


class Ocaml(Language):
    ext = "ml"


class Perl(Language):
    ext = "pl"


class PHP(Language):
    ext = "php"


class Python(Language):
    ext = "py"
    mco = True

    recipe = {
        "build": [],
        "run": "python {filename}",
    }


class Ruby(Language):
    ext = "rb"


class Rust(Language):
    ext = "rs"


class Scala(Language):
    ext = "scala"
    output = "Main"


class Swift(Language):
    ext = "swift"


class TypeScript(Language):
    ext = "ts"
    mco = True
    output = "a.js"
