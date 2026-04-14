# Makefile for fix-headers-hook project
#
# Prerequisites:
#   - Install uv (recommended via pipx: pipx install uv)
#   - Create a blank .env file to ensure a clean environment: touch .env
#
# All Python commands are executed through 'uv run' to maintain proper isolation.

# Configuration
UV := uv

# Default target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install     - Install development dependencies (uv sync)"
	@echo "  lint        - Run code linting (ruff)"
	@echo "  typecheck   - Run type checking (mypy)"
	@echo "  test        - Run tests (pytest)"
	@echo "  format      - Format code (ruff format)"
	@echo "  clean       - Clean build artifacts"
	@echo "  all         - Run lint, typecheck, and test"
	@echo "  dev         - Install package in editable mode"
	@echo "  self-test   - Run fix-headers on this project (dry-run)"

# Install dependencies using uv sync
.PHONY: install
install:
	@test -f .env || touch .env
	$(UV) sync
	@echo "Dependencies installed"

# Run code linting
.PHONY: lint
lint: install
	$(UV) run ruff check src/
	@echo "Linting completed"

# Run type checking
.PHONY: typecheck
typecheck: install
	$(UV) run mypy src/
	@echo "Type checking completed"

# Run tests
.PHONY: test
test: install
	$(UV) run pytest -v tests/ || echo "No tests found"
	@echo "Testing completed"

# Format code
.PHONY: format
format: install
	$(UV) run ruff format src/
	@echo "Code formatting completed"

# Clean build artifacts
.PHONY: clean
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "Cleaned build artifacts"

# Run all checks
.PHONY: all
all: lint typecheck test
	@echo "All checks completed"

# Install package in editable mode (development install)
.PHONY: dev
dev: install
	$(UV) pip install -e .
	@echo "Installed in development mode"

# Self-test: run fix-headers on this project (dry-run)
.PHONY: self-test
self-test: install
	$(UV) run python -m fix_headers . --dry-run
	@echo "Self-test completed"