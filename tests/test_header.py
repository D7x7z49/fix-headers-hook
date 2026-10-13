# @path[tests/test_header.py]

from fix_headers_hook.core import is_header_line, is_legacy_header_line


def test_marked_header_hash():
    assert is_header_line("# @path[a/b.py]", "#", "")
    assert not is_header_line("# a/b.py", "#", "")


def test_marked_header_html():
    assert is_header_line("<!-- @path[a.md] -->", "<!--", "-->")
    assert not is_header_line("<!-- a.md -->", "<!--", "-->")


def test_legacy_header_hash():
    assert is_legacy_header_line("# a/b.py", "#", "")
    assert is_legacy_header_line("# module.py", "#", "")


def test_legacy_header_html():
    assert is_legacy_header_line("<!-- README.md -->", "<!--", "-->")


def test_legacy_rejects_non_path_comment():
    assert not is_legacy_header_line("# 2.0", "#", "")
    assert not is_legacy_header_line("# see util.py", "#", "")
    assert not is_legacy_header_line("# noqa", "#", "")


def test_non_comment_is_not_header():
    assert not is_header_line("x = '@path[a.py]'", "#", "")
    assert not is_legacy_header_line('x = "a.py"', "#", "")
