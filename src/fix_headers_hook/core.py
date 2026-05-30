# src/fix_headers_hook/core.py
# src/fix_headers/core.py

import json
from pathlib import Path
from typing import Optional

from .constants import COMMENT_STYLES
from .files import collect_target_files
from .root import get_project_root


def get_comment_line(path: Path) -> Optional[str]:
    """Return the expected header comment line for a file, or None if unsupported."""
    root = get_project_root()
    rel = path.resolve().relative_to(root).as_posix()

    for template, suffixes in COMMENT_STYLES:
        for suffix in suffixes:
            if path.suffix == f".{suffix}":
                return template.format(rel=rel)
    return None


def process_file(path: Path) -> str:
    """Fix the header of a single file.

    Returns one of: "added", "modified", "skipped".
    """
    comment_line = get_comment_line(path)
    if comment_line is None:
        return "skipped"

    data = path.read_text()
    lines = data.splitlines()

    # empty file: just write the header
    if len(lines) == 0:
        path.write_text(f"{comment_line}\n")
        return "added"

    # header already correct (first line, or after shebang)
    if lines[0].strip() == comment_line:
        return "skipped"

    # no shebang: insert at line 0
    if not lines[0].startswith("#!"):
        lines.insert(0, comment_line)
        path.write_text("\n".join(lines) + "\n")
        return "modified"

    # shebang present: header should be on line 1
    if len(lines) >= 2 and lines[1].strip() == comment_line:
        return "skipped"

    lines.insert(1, comment_line)
    path.write_text("\n".join(lines) + "\n")
    return "modified"


def fix_headers(
    paths: list[str] | None = None,
    *,
    dry_run: bool = False,
    quiet: bool = False,
) -> int:
    """Main entry point: collect files and fix their headers.

    Args:
        paths: File or directory paths to process. None means current directory.
        dry_run: If True, only print what would be done, do not modify files.
        quiet: If True, suppress per-file output.

    Returns:
        Number of files modified (0 = all clean).
    """
    if paths is None:
        paths = ["."]

    file_paths = [Path(p) for p in paths]
    target_files = collect_target_files(file_paths)

    if not target_files:
        if not quiet:
            print("[*] No files to process")
        return 0

    stats = {"added": 0, "modified": 0, "skipped": 0, "error": 0}

    for file_path in sorted(target_files):
        try:
            if dry_run:
                operation = "skipped"
                print(f"[*] would fix {file_path}")
            else:
                operation = process_file(file_path)
        except Exception as e:
            operation = "error"
            if not quiet:
                print(f"[!] {file_path}: {e}")

        stats[operation] += 1

    if not quiet:
        print(f"[*] {json.dumps(stats)}")

    return stats["added"] + stats["modified"]
