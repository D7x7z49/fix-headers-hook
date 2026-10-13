# @path[src/fix_headers_hook/root.py]

from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def get_project_root() -> Path:
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / ".git").is_dir():
            return parent

    raise RuntimeError(
        "could not find project root (no .git directory found above current dir)"
    )
