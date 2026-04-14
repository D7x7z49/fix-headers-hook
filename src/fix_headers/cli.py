"""
Command line interface for fix_headers.
"""

import argparse
import sys
from pathlib import Path
from typing import List

from .core import fix_headers


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Add/update file headers with relative path comments.",
        epilog="If no paths given, processes current directory recursively.",
    )
    parser.add_argument("paths", nargs="*", help="Files or directories to process")
    parser.add_argument(
        "--root", help="Project root directory (auto-detected if not given)"
    )
    parser.add_argument(
        "--ignore", action="append", default=[], help="Additional ignore patterns"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Only show what would be done"
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Suppress [*] output (skipped files)"
    )
    parser.add_argument("--version", action="version", version="fix-headers 0.1.0")

    return parser.parse_args()


def main() -> None:
    """
    Main entry point for CLI.
    """
    args = parse_args()

    try:
        # Convert paths to strings
        paths: List[str] = (
            [str(Path(p).resolve()) for p in args.paths] if args.paths else []
        )

        # Call the main function
        stats = fix_headers(
            paths=paths,
            root=args.root,
            ignore_patterns=args.ignore,
            dry_run=args.dry_run,
            quiet=args.quiet,
        )

        # Set exit code based on errors
        if stats["error"] > 0:
            sys.exit(1)
        elif args.dry_run and stats["modified"] > 0:
            # In dry-run mode, exit with 1 if modifications would be made
            # This is useful for CI/CD pipelines
            sys.exit(1)
        else:
            sys.exit(0)

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
