# tests/test_files.py

from pathlib import Path

from fix_headers_hook.files import collect_target_files, should_ignore_dir


def test_collect_supported_files(make_file):
    make_file("a.py", "")
    make_file("b.js", "")
    make_file("c.png", "")
    make_file("d.go", "")

    files = collect_target_files([Path(".")])
    names = {f.name for f in files}
    assert names == {"a.py", "b.js", "d.go"}


def test_collect_from_directory(make_file):
    make_file("src/a.py", "")
    make_file("src/b.py", "")
    make_file("other/c.py", "")

    files = collect_target_files([Path("src")])
    names = {f.name for f in files}
    assert names == {"a.py", "b.py"}


def test_excludes_ignored_dirs(make_file):
    make_file(".venv/lib/module.py", "")
    make_file("node_modules/pkg/index.js", "")
    make_file("dist/bundle.min.js", "")
    make_file("build/output.py", "")
    make_file("src/main.py", "")

    files = collect_target_files([Path(".")])
    names = {f.name for f in files}
    assert names == {"main.py"}


def test_respects_gitignore(make_file):
    make_file(".gitignore", "generated.py\n")
    make_file("src/main.py", "")
    make_file("generated.py", "")

    files = collect_target_files([Path(".")])
    names = {f.name for f in files}
    assert names == {"main.py"}


def test_should_ignore_dir():
    assert should_ignore_dir(Path(".venv/lib/module.py"))
    assert should_ignore_dir(Path("node_modules/pkg/index.js"))
    assert not should_ignore_dir(Path("src/main.py"))
