# @path[src/fix_headers_hook/constants.py]

# marker that tags a managed header. the relative path sits inside the
# brackets, so the path has an explicit start and end.
MARKER = "@path"

# (comment prefix, comment suffix, file suffixes)
# fmt: off
COMMENT_STYLES: list[tuple[str, str, list[str]]] = [
    ("#", "", [
        "py", "pyw", "pyx", "pxd", "pxi",      # Python / Cython
        "sh", "bash", "zsh", "fish", "ksh",    # shell
        "ps1", "psm1", "psd1",                 # PowerShell
        "pl", "pm", "t",                       # Perl
        "rb", "rake", "gemspec",               # Ruby
        "php", "phtml",                        # PHP
        "yaml", "yml",                         # YAML
        "toml",                                # TOML
        "ini", "cfg", "conf", "cnf",           # config / INI
        "env", "envrc",                        # env files
        "hcl", "tf", "tfvars",                 # HashiCorp / Terraform
        "r", "rprofile",                       # R
        "makefile", "dockerfile",              # special filenames as suffix
        "properties", "editorconfig", "gitignore", "gitattributes", "wal"
    ]),
    ("//", "", [
        "c", "h", "cpp", "cxx", "cc", "hpp", "hxx", "hh", # C / C++
        "java", "kt", "kts", "groovy", "gradle", "scala", # JVM
        "js", "mjs", "cjs", "ts", "tsx", "jsx",           # JavaScript
        "go",               # Go
        "rs",               # Rust
        "swift",            # Swift
        "cs",               # C#
        "dart",             # Dart
        "json5", "jsonc",   # JSON with comments
        "proto",            # Protobuf
    ]),
    ("--", "", [
        "sql", "psql", "mysql", # SQL dialects
        "lua",                  # Lua
        "hs", "lhs",            # Haskell
        "ada", "adb", "ads",    # Ada
        "elm",                  # Elm
        "vhd", "vhdl",          # VHDL
    ]),
    ("<!--", "-->", [
        "html", "htm", "xhtml", "xml", "xsl", "xslt", "svg", # HTML & XML
        "md", "markdown",   # Markdown
    ]),
    ("/*", "*/", [
        "css", "scss", "sass", "less", "pcss", # CSS & pre-processors
    ]),
    (";", "", [
        "asm", "s", "nasm", "inc", # assembly
    ]),
]
# fmt: on

SUFFIX_SET: set[str] = {
    suffix for _, _, suffixes in COMMENT_STYLES for suffix in suffixes
}

IGNORE_DIRS: set[str] = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".cache",
    ".idea",
    ".vscode",
}
