# fix-headers-hook

A pre-commit hook to add/update file headers with relative path comments.

## Features

- Adds or updates file headers with relative path comments
- Supports multiple file types (Python, shell scripts, config files, etc.)
- Respects `.gitignore` patterns
- Detects shebang lines and preserves them
- Works as both a standalone CLI tool and a pre-commit hook
- Dry-run mode for previewing changes

## Supported File Types

- Python (.py)
- Shell scripts (.sh, .bash, .zsh, .fish, .ps1)
- Perl (.pl)
- Ruby (.rb)
- PHP (.php)
- Configuration files (.yaml, .yml, .toml, .ini, .cfg, .conf, .env, .json5, .hcl)
- Terraform (.tf)
- SQL (.sql)
- Lua (.lua)
- Special files: Makefile, Dockerfile

## Installation

### As a pre-commit hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/yourusername/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
```

## Usage

### As a pre-commit hook

The hook will automatically run on staged files during `git commit`.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/fix-headers-hook
cd fix-headers-hook

# Create virtual environment and install dependencies
make install

# Install in development mode
make dev
```

### Available Commands

```bash
# Run all checks (lint, typecheck, test)
make all

# Run code linting
make lint

# Run type checking
make typecheck

# Format code
make format

# Run tests
make test

# Clean build artifacts
make clean

# Self-test: run fix-headers on this project
make self-test
```

## Configuration

The tool automatically:
- Detects project root by looking for `.git` or `pyproject.toml`
- Reads `.gitignore` patterns
- Ignores common directories (`.git`, `node_modules`, `.venv`, etc.)

## How It Works

1. For each supported file, the tool calculates its relative path from the project root
2. If the file has a shebang line, the header is inserted after it
3. If the file already has a header in the expected format, it's skipped
4. Otherwise, the header is added or updated

Example header: `# src/fix_headers/core.py`

## License

MIT License - see LICENSE file for details.