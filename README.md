<!-- README.md -->
# fix-headers-hook

A pre-commit hook that adds or updates file header comments with relative path information.

## Features

- Adds or updates file headers automatically on `git commit`
- Supports 50+ file types across 6 comment syntax families
- Respects `.gitignore` patterns and common ignore directories
- Preserves shebang lines
- Dry-run mode for preview
- Idempotent — safe to run repeatedly

## Supported File Types

Six comment syntax families across 50+ extensions.

Hash-style (`# {rel}`):
`.py` `.sh` `.bash` `.zsh` `.yaml` `.yml` `.toml` `.ini` `.cfg` `.rb` `.php` `.pl` `.r` `.tf` `.hcl` `.env` `Makefile` `Dockerfile` and more.

Slash-style (`// {rel}`):
`.js` `.ts` `.jsx` `.tsx` `.go` `.rs` `.swift` `.cs` `.java` `.kt` `.scala` `.c` `.cpp` `.h` `.dart` `.proto` and more.

Dash-style (`-- {rel}`):
`.sql` `.lua` `.hs` `.elm` `.vhd` `.vhdl` `.ada` and more.

HTML-style (`<!-- {rel} -->`):
`.html` `.xml` `.svg` `.md` `.markdown` and more.

Block-style (`/* {rel} */`):
`.css` `.scss` `.sass` `.less` and more.

Semicolon-style (`; {rel}`):
`.asm` `.s` `.nasm` and more.

## Installation

Add to your `.pre-commit-config.yaml`, then run `pre-commit install`.

Apply to all supported files in the repository:

```yaml
repos:
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
```

Limit to specific directories with a `files` pattern:

```yaml
repos:
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
        files: ^(src|tests|scripts)/
```

Exclude generated or vendored paths:

```yaml
repos:
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
        exclude: ^(vendor|generated|\.venv)/
```

## Safety and Scoping

- The hook only touches files whose extensions it recognizes. Unsupported files are silently skipped.
- Directories in `.gitignore` and common ignore paths (`.venv`, `node_modules`, `build`, `dist` ...) are never touched.
- Shebang lines are preserved.
- Run `pre-commit run fix-headers --all-files` to preview what would change before committing.
- If unsure, start with a narrow `files` pattern and widen gradually.

## Usage

Once installed, the hook runs automatically on staged files during `git commit`.

To preview changes without committing:

```bash
pre-commit run fix-headers --all-files
```

To run the tool directly (outside pre-commit):

```bash
fix-headers src/ --dry-run    # preview
fix-headers src/              # apply
```

## How It Works

1. For each supported file, the tool computes its relative path from the project root
2. If the file has a shebang line, the header is inserted after it
3. If the file already has the correct header, it is skipped
4. Otherwise, the header is added or updated

Example: a file at `src/utils/helper.py` gets the header `# src/utils/helper.py`.

## Development

See `make help` for all available targets.

Quick start:

```bash
make install          # sync dependencies
make all              # lint + typecheck + test
make hook-test        # run all pre-commit hooks on all files
make self-test        # dry-run fix-headers on own source
```

Development dependencies are declared in `pyproject.toml` under the `dev` extras group. Python version is pinned in `.python-version`.

## License

MIT License — see `LICENSE`.
