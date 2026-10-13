# @path[src/fix_headers_hook/files.py]

import fnmatch
from pathlib import Path

from .constants import IGNORE_DIRS, SUFFIX_SET
from .root import get_project_root


def load_gitignore_patterns() -> list[str]:
    gitignore = get_project_root() / ".gitignore"
    if not gitignore.exists():
        return []

    patterns: list[str] = []
    for line in gitignore.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("!"):
            patterns.append(line)
    return patterns


def should_exclude(path: Path, patterns: list[str]) -> bool:
    try:
        rel = str(path.relative_to(get_project_root()))
    except ValueError:
        rel = str(path)

    for pattern in patterns:
        if pattern.endswith("/"):
            directory = pattern.rstrip("/")
            if fnmatch.fnmatch(rel, f"{directory}/*") or fnmatch.fnmatch(
                rel, f"**/{directory}/*"
            ):
                return True
        elif pattern.startswith("/"):
            if fnmatch.fnmatch(rel, pattern[1:]) or fnmatch.fnmatch(
                rel, f"**/{pattern[1:]}"
            ):
                return True
        elif fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(rel, f"**/{pattern}"):
            return True

    return False


def should_ignore_dir(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def collect_target_files(paths: list[Path]) -> set[Path]:
    target_files: set[Path] = set()
    patterns = load_gitignore_patterns()

    for path in paths:
        if path.is_file():
            if (
                path.suffix.lstrip(".") in SUFFIX_SET
                and not should_ignore_dir(path)
                and not should_exclude(path, patterns)
            ):
                target_files.add(path)
        elif path.is_dir():
            for file_path in path.rglob("*"):
                if (
                    file_path.is_file()
                    and file_path.suffix.lstrip(".") in SUFFIX_SET
                    and not should_ignore_dir(file_path)
                    and not should_exclude(file_path, patterns)
                ):
                    target_files.add(file_path)

    return target_files
