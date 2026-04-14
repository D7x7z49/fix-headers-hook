"""
fix_headers package.

A pre-commit hook to add/update file headers with relative path comments.
"""

__version__ = "0.1.0"
__author__ = "DevK"
__description__ = (
    "pre-commit hook to add/update file headers with relative path comments"
)

from .cli import main
from .core import (
    collect_files,
    fix_headers,
    get_project_root,
    is_supported,
    load_gitignore,
    process_file,
    read_file_lines,
    should_ignore,
    write_file_lines,
)

__all__ = [
    "get_project_root",
    "load_gitignore",
    "should_ignore",
    "collect_files",
    "is_supported",
    "read_file_lines",
    "write_file_lines",
    "process_file",
    "fix_headers",
    "main",
]
