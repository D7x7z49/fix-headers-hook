<!-- AGENTS.md -->
<!-- Project conventions and guidelines for fix-headers-hook -->

PROJECT IDENTITY

- A Python pre-commit hook that adds or updates file header comments with relative path information.
- Distributed as a pre-commit hook via `.pre-commit-hooks.yaml`; consumed by the pre-commit framework.
- The project dogfoods its own hook via `.pre-commit-config.yaml`.

TOOL STACK

- Package manager: `uv` — all Python commands run through `uv run` or an activated `.venv`.
- Build backend: `uv_build`.
- Task runner: `Makefile` — the authoritative entry point for common dev workflows.
- Linter and formatter: `ruff`.
- Type checker: `mypy`.
- Test runner: `pytest`.

PROJECT FILES

- `pyproject.toml` — project metadata, dependencies (dev extras), and tool configs.
- `Makefile` — task definitions (`install`, `lint`, `format`, `test`, `hook-test`, etc.).
- `.pre-commit-hooks.yaml` — hook definition for downstream consumers.
- `.pre-commit-config.yaml` — local pre-commit setup for self-validation.
- `.python-version` — pinned Python version for development.

SOURCE CONVENTIONS

- Source code lives under `src/fix_headers_hook/`.
- Tests live under `tests/`.
- Write code comments and commit messages in english.
- Use `uv run` prefix for all Python commands unless the venv is activated.
- Run `make hook-test` before committing to ensure all pre-commit hooks pass.

TESTING

- Test philosophy: see `tests/README.md`.
- Run tests via `make test` or `uv run pytest`.
- Coverage reports available through `make test-cov`.

---
