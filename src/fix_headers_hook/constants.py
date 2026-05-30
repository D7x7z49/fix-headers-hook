# src/fix_headers_hook/constants.py
# src/fix_headers/constants.py

# fmt: off
COMMENT_STYLES: list[tuple[str, list[str]]] = [
    ("# {rel}", [
        "py", "pyw", "pyx", "pxd", "pxi",      # Python / Cython
        "sh", "bash", "zsh", "fish", "ksh",    # Shell
        "ps1", "psm1", "psd1",                 # PowerShell
        "pl", "pm", "t",                       # Perl
        "rb", "rake", "gemspec",               # Ruby
        "php", "phtml",                        # PHP
        "yaml", "yml",                         # YAML
        "toml",                                # TOML
        "ini", "cfg", "conf", "cnf",           # Config / INI
        "env", "envrc",                        # Env files
        "hcl", "tf", "tfvars",                 # HashiCorp / Terraform
        "r", "rprofile",                       # R
        "makefile", "dockerfile",              # Special filenames as suffix
        "properties", "editorconfig", "gitignore", "gitattributes", "wal"
    ]),
    ("// {rel}", [
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
    ("-- {rel}", [
        "sql", "psql", "mysql", # SQL dialects
        "lua",                  # Lua
        "hs", "lhs",            # Haskell
        "ada", "adb", "ads",    # Ada
        "elm",                  # Elm
        "vhd", "vhdl",          # VHDL
    ]),
    ("<!-- {rel} -->", [
        "html", "htm", "xhtml", "xml", "xsl", "xslt", "svg", # HTML & XML
        "md", "markdown",   # Markdown
    ]),
    ("/* {rel} */", [
        "css", "scss", "sass", "less", "pcss", # CSS & pre-processors
    ]),
    ("; {rel}", [
        "asm", "s", "nasm", "inc", # Assembly
    ]),
]
# fmt: on

SUFFIX_SET: set[str] = {suffix for _, suffixes in COMMENT_STYLES for suffix in suffixes}

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
