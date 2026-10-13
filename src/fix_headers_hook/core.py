# @path[src/fix_headers_hook/core.py]

import json
from pathlib import Path
from typing import Optional

from .constants import COMMENT_STYLES, MARKER, SUFFIX_SET
from .files import collect_target_files
from .root import get_project_root


def get_comment_style(path: Path) -> Optional[tuple[str, str]]:
    for prefix, suffix, suffixes in COMMENT_STYLES:
        if path.suffix.lstrip(".") in suffixes:
            return prefix, suffix
    return None


def render_header(prefix: str, suffix: str, rel: str) -> str:
    parts = (prefix, f"{MARKER}[{rel}]", suffix)
    return " ".join(part for part in parts if part)


def get_comment_line(path: Path) -> Optional[str]:
    style = get_comment_style(path)
    if style is None:
        return None

    prefix, suffix = style
    rel = path.resolve().relative_to(get_project_root()).as_posix()
    return render_header(prefix, suffix, rel)


def strip_comment(line: str, prefix: str, suffix: str) -> Optional[str]:
    stripped = line.strip()
    if not stripped.startswith(prefix):
        return None

    body = stripped[len(prefix) :]
    if suffix:
        if not body.endswith(suffix):
            return None
        body = body[: -len(suffix)]
    return body.strip()


def is_header_line(line: str, prefix: str, suffix: str) -> bool:
    body = strip_comment(line, prefix, suffix)
    if body is None:
        return False
    return body.startswith(MARKER) and body.endswith("]")


def is_legacy_header_line(line: str, prefix: str, suffix: str) -> bool:
    # legacy headers are bare paths: a single token with a known suffix
    body = strip_comment(line, prefix, suffix)
    if body is None or " " in body:
        return False
    return body.rsplit(".", 1)[-1] in SUFFIX_SET


def process_file(path: Path) -> str:
    # returns one of "added", "modified", or "skipped"
    style = get_comment_style(path)
    if style is None:
        return "skipped"

    comment_line = get_comment_line(path)
    assert comment_line is not None

    data = path.read_text()
    lines = data.splitlines()

    # empty file: just write the header
    if len(lines) == 0:
        path.write_text(f"{comment_line}\n")
        return "added"

    # header sits on line 0, or line 1 when a shebang is present
    index = 1 if lines[0].startswith("#!") else 0

    # replace a run of existing headers (marked or legacy) with one clean line
    end = index
    while end < len(lines) and (
        is_header_line(lines[end], *style) or is_legacy_header_line(lines[end], *style)
    ):
        end += 1

    if lines[index:end] == [comment_line]:
        return "skipped"

    lines[index:end] = [comment_line]
    path.write_text("\n".join(lines) + "\n")
    return "modified"


def fix_headers(
    paths: list[str] | None = None,
    *,
    dry_run: bool = False,
    quiet: bool = False,
) -> int:
    # returns the number of files modified (0 = all clean)
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
