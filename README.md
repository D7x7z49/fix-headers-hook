# fix-headers-hook

A pre-commit hook to add/update file headers with relative path comments.

## Features

- Adds or updates file headers with relative path comments
- Supports multiple file types (Python, shell scripts, config files, etc.)
- Respects `.gitignore` patterns
- Detects shebang lines and preserves them
- Dry-run mode for previewing changes
- Seamless integration with pre-commit framework

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
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
```

## Usage

### As a pre-commit hook

The hook automatically processes staged files during `git commit`. It adds or updates file headers with the relative path from the project root.

1. Add to your `.pre-commit-config.yaml` as shown in the Installation section
2. Install the hook: `pre-commit install`
3. Commit files normally: `git add file.py && git commit -m "message"`

The hook will:
- Process Python files, shell scripts, configuration files, and more
- Insert headers after shebang lines when present
- Skip files already containing correct headers
- Respect your `.gitignore` patterns
- Show a summary of changes made

Example transformation:
- Before: Plain Python file without header
- After: File with `# src/module/file.py` comment on first line (or second line if shebang present)

To preview changes without modifying files, use:
```bash
pre-commit run fix-headers --all-files --hook-stage pre-commit
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/D7x7z49/fix-headers-hook
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