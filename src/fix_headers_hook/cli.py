# src/fix_headers_hook/cli.py
# src/fix_headers/cli.py

import argparse
import sys

from .core import fix_headers


def main() -> None:
    parser = argparse.ArgumentParser(description="check or fix file header comments")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="file or directory to process (default: current directory)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="suppress per-file output, only show summary",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would be done without modifying files",
    )

    args = parser.parse_args()

    try:
        modified = fix_headers(
            paths=args.paths,
            dry_run=args.dry_run,
            quiet=args.quiet,
        )
        if args.dry_run and modified > 0:
            sys.exit(1)
    except RuntimeError as e:
        print(f"[!] {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] cancelled", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
