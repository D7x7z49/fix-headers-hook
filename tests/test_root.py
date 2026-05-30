# tests/test_root.py

import os
import shutil
import tempfile
from pathlib import Path

import pytest

from fix_headers_hook.root import get_project_root


def test_finds_git_dir(tmp_git_repo: Path):
    root = get_project_root()
    assert root == tmp_git_repo.resolve()
    assert (root / ".git").is_dir()


def test_not_in_git_dir_raises():
    old = Path.cwd()
    nodir = Path(tempfile.mkdtemp())
    try:
        os.chdir(nodir)
        get_project_root.cache_clear()
        with pytest.raises(RuntimeError, match="could not find project root"):
            get_project_root()
    finally:
        os.chdir(old)
        shutil.rmtree(nodir, ignore_errors=True)
