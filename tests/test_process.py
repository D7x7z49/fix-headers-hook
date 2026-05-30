# tests/test_process.py

from fix_headers_hook.core import process_file


def test_empty_file(make_file):
    f = make_file("empty.py", "")
    result = process_file(f)
    assert result == "added"
    assert f.read_text() == "# empty.py\n"


def test_no_header(make_file):
    f = make_file("mod.py", "x = 1\n")
    result = process_file(f)
    assert result == "modified"
    lines = f.read_text().splitlines()
    assert lines[0] == "# mod.py"
    assert lines[1] == "x = 1"


def test_already_correct(make_file):
    f = make_file("mod.py", "# mod.py\nx = 1\n")
    result = process_file(f)
    assert result == "skipped"
    assert f.read_text() == "# mod.py\nx = 1\n"


def test_shebang_preserved(make_file):
    f = make_file("script.sh", "#!/bin/bash\necho hello\n")
    result = process_file(f)
    assert result == "modified"
    lines = f.read_text().splitlines()
    assert lines[0] == "#!/bin/bash"
    assert lines[1] == "# script.sh"
    assert lines[2] == "echo hello"


def test_shebang_already_correct(make_file):
    f = make_file("script.sh", "#!/bin/bash\n# script.sh\necho hello\n")
    result = process_file(f)
    assert result == "skipped"


def test_replaces_wrong_header(make_file):
    f = make_file("mod.py", "# old/wrong.py\nx = 1\n")
    result = process_file(f)
    assert result == "modified"
    lines = f.read_text().splitlines()
    assert lines[0] == "# mod.py"


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
