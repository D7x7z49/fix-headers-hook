# AGENTS.md - fix-headers-hook

This project is a Python pre-commit hook. It adds or updates file header comments containing relative path information. The tool uses `uv` as its package manager. A `Makefile` supplies a convenient command scaffold for common development tasks.

Before executing any Python command, prefix it with `uv run`. This ensures the correct virtual environment is used. Alternatively, activate the environment first with `source .venv/bin/activate`.

For a quick test of the hook on the current directory:

- Run `uv run python -m fix_headers . --dry-run`.

The `Makefile` orchestrates most daily workflows. Use these targets for setup and quality checks:

- `make install` — Creates the virtual environment and installs dependencies via `uv`.
- `make lint` — Checks code style with `ruff`.
- `make typecheck` — Verifies type hints with `mypy`.
- `make format` — Automatically formats the source code.
- `make all` — Runs linting, type checking, and the test placeholder in sequence.
- `make self-test` — Demonstrates how the hook behaves on this project in dry-run mode.

When examining or editing the `Makefile`, note that the `PYTHON` variable should refer to `.venv/bin/python`. Alternatively, commands may rely directly on `uv run`.

The tool's entry point is `fix_headers.cli:main`. After installation, it is invoked as `fix-headers`.

This package is designed as a pre-commit hook, not a standalone application. The hook definition resides in `.pre-commit-hooks.yaml`. The self-test configuration lives in `.pre-commit-config.yaml` with local dry-run settings.

A dedicated tests directory does not yet exist. Consequently, the `make test` target will report "No tests found". The minimum required Python version is 3.12.
