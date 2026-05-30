# tests/conftest.py

import os
import shutil
import tempfile
from pathlib import Path

import pytest

from fix_headers_hook.root import get_project_root


@pytest.fixture(autouse=True)
def _clear_root_cache() -> None:
    """Clear the project root cache before each test."""
    get_project_root.cache_clear()


@pytest.fixture
def tmp_git_repo() -> Path:
    """Create a temporary git repository and chdir into it."""
    old_cwd = Path.cwd()
    tmpdir = Path(tempfile.mkdtemp())
    os.chdir(tmpdir)
    os.system("git init -q")
    os.system("git config user.email test@test.com")
    os.system("git config user.name test")

    yield tmpdir

    os.chdir(old_cwd)
    shutil.rmtree(tmpdir, ignore_errors=True)


@pytest.fixture
def make_file(tmp_git_repo: Path):
    """Factory to create files in the temp repo."""

    def _make(path: str, content: str) -> Path:
        full = tmp_git_repo / path
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content)
        return full

    return _make
