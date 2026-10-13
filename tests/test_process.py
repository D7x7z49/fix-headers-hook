# @path[tests/test_process.py]

from fix_headers_hook.core import process_file


def test_empty_file(make_file):
    f = make_file("empty.py", "")
    result = process_file(f)
    assert result == "added"
    assert f.read_text() == "# @path[empty.py]\n"


def test_no_header(make_file):
    f = make_file("mod.py", "x = 1\n")
    result = process_file(f)
    assert result == "modified"
    assert f.read_text() == "# @path[mod.py]\nx = 1\n"


def test_already_correct(make_file):
    f = make_file("mod.py", "# @path[mod.py]\nx = 1\n")
    result = process_file(f)
    assert result == "skipped"
    assert f.read_text() == "# @path[mod.py]\nx = 1\n"


def test_stale_marker_replaced(make_file):
    f = make_file("mod.py", "# @path[old/loc.py]\nx = 1\n")
    result = process_file(f)
    assert result == "modified"
    assert f.read_text() == "# @path[mod.py]\nx = 1\n"


def test_legacy_header_replaced(make_file):
    f = make_file("mod.py", "# old/wrong.py\nx = 1\n")
    result = process_file(f)
    assert result == "modified"
    assert f.read_text() == "# @path[mod.py]\nx = 1\n"


def test_duplicate_headers_collapsed(make_file):
    f = make_file("mod.py", "# @path[mod.py]\n# old/wrong.py\nx = 1\n")
    result = process_file(f)
    assert result == "modified"
    assert f.read_text() == "# @path[mod.py]\nx = 1\n"


def test_plain_comment_kept(make_file):
    f = make_file("mod.py", "# type: ignore\nx = 1\n")
    result = process_file(f)
    assert result == "modified"
    assert f.read_text() == "# @path[mod.py]\n# type: ignore\nx = 1\n"


def test_shebang_preserved(make_file):
    f = make_file("script.sh", "#!/bin/bash\necho hello\n")
    result = process_file(f)
    assert result == "modified"
    assert f.read_text() == "#!/bin/bash\n# @path[script.sh]\necho hello\n"


def test_shebang_already_correct(make_file):
    f = make_file("script.sh", "#!/bin/bash\n# @path[script.sh]\necho hello\n")
    result = process_file(f)
    assert result == "skipped"


def test_idempotent(make_file):
    f = make_file("mod.py", "x = 1\n")
    process_file(f)
    result = process_file(f)
    assert result == "skipped"


def test_unsupported_file(make_file):
    f = make_file("img.png", "binary")
    result = process_file(f)
    assert result == "skipped"
    assert f.read_text() == "binary"
