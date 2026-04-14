"""
Utility functions for fix_headers.
"""

import os
from pathlib import Path
from typing import List


def matches_any_pattern(path: Path, patterns: List[str]) -> bool:
    """
    Check if a path matches any of the given patterns.

    Args:
        path: Path to check
        patterns: List of glob patterns

    Returns:
        True if path matches any pattern
    """
    import fnmatch

    path_str = path.as_posix()
    return any(fnmatch.fnmatch(path_str, pattern) for pattern in patterns)


def normalize_path(path: str) -> str:
    """
    Normalize a file path.

    Args:
        path: Path to normalize

    Returns:
        Normalized path
    """
    return os.path.normpath(path)
