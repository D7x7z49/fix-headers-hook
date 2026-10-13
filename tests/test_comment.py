# @path[tests/test_comment.py]

from fix_headers_hook.core import get_comment_line


def test_python_comment(make_file):
    f = make_file("src/module.py", "")
    assert get_comment_line(f) == "# @path[src/module.py]"


def test_javascript_comment(make_file):
    f = make_file("src/app.js", "")
    assert get_comment_line(f) == "// @path[src/app.js]"


def test_typescript_comment(make_file):
    f = make_file("src/app.ts", "")
    assert get_comment_line(f) == "// @path[src/app.ts]"


def test_go_comment(make_file):
    f = make_file("main.go", "")
    assert get_comment_line(f) == "// @path[main.go]"


def test_rust_comment(make_file):
    f = make_file("src/main.rs", "")
    assert get_comment_line(f) == "// @path[src/main.rs]"


def test_sql_comment(make_file):
    f = make_file("query.sql", "")
    assert get_comment_line(f) == "-- @path[query.sql]"


def test_lua_comment(make_file):
    f = make_file("init.lua", "")
    assert get_comment_line(f) == "-- @path[init.lua]"


def test_html_comment(make_file):
    f = make_file("index.html", "")
    assert get_comment_line(f) == "<!-- @path[index.html] -->"


def test_markdown_comment(make_file):
    f = make_file("README.md", "")
    assert get_comment_line(f) == "<!-- @path[README.md] -->"


def test_css_comment(make_file):
    f = make_file("style.css", "")
    assert get_comment_line(f) == "/* @path[style.css] */"


def test_asm_comment(make_file):
    f = make_file("boot.asm", "")
    assert get_comment_line(f) == "; @path[boot.asm]"


def test_yaml_comment(make_file):
    f = make_file("config.yaml", "")
    assert get_comment_line(f) == "# @path[config.yaml]"


def test_toml_comment(make_file):
    f = make_file("pyproject.toml", "")
    assert get_comment_line(f) == "# @path[pyproject.toml]"


def test_sh_comment(make_file):
    f = make_file("script.sh", "")
    assert get_comment_line(f) == "# @path[script.sh]"


def test_unsupported_type(make_file):
    f = make_file("image.png", "")
    assert get_comment_line(f) is None


def test_deep_path(make_file):
    f = make_file("a/b/c/d/e/util.py", "")
    assert get_comment_line(f) == "# @path[a/b/c/d/e/util.py]"
