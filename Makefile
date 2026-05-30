# Makefile for fix-headers-hook

.PHONY: help install lint typecheck format test test-cov clean all dev \
        hook-test hook-install self-test self-test-apply

help:  ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  %-16s %s\n", $$1, $$2}'

install:  ## install dependencies with uv
	uv sync --extra dev

lint:  ## run ruff linter
	uv run ruff check src/ tests/

typecheck:  ## run mypy
	uv run mypy src/

format:  ## format code with ruff
	uv run ruff format src/ tests/

test:  ## run tests
	uv run pytest -v tests/

test-cov:  ## run tests with coverage report
	uv run pytest -v --cov=fix_headers_hook --cov-report=term-missing tests/

clean:  ## remove build artifacts and caches
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true

all: lint typecheck test  ## run all checks

hook-test:  ## run all pre-commit hooks on all files (dry-run)
	uv run pre-commit run --all-files

hook-install:  ## install pre-commit hooks into .git
	uv run pre-commit install --install-hooks

dev: install  ## install in editable mode
	uv pip install -e .

self-test:  ## run fix-headers on own source (dry-run)
	uv run python -m fix_headers_hook src/ tests/ --dry-run

self-test-apply:  ## run fix-headers on own source (apply)
	uv run python -m fix_headers_hook src/ tests/
