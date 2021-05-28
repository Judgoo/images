class Language:
    filestem: str = "main"
    ext: str = "txt"
    # 只为编译型语言设置的字段
    output: str = "a.out"
    mco: bool = False

    @classmethod
    @property
    def filename(cls):
        return f"{cls.filestem}.{cls.ext}"

    @classmethod
    def to_dict(cls):
        return {
            "filestem": cls.filestem,
            "filename": cls.filename,
            "ext": cls.ext,
            "output": cls.output,
            "mco": cls.mco,
        }


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
