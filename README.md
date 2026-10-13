<!-- @path[README.md] -->
# fix-headers-hook

a pre-commit hook that adds or updates file header comments with relative path information.

## Features

- adds or updates file headers automatically on `git commit`
- supports 50+ file types across 6 comment syntax families
- respects `.gitignore` patterns and common ignore directories
- preserves shebang lines
- dry-run mode for preview
- idempotent — safe to run repeatedly
- tracks renames and moves via a `@path[...]` marker

## Supported File Types

six comment syntax families across 50+ extensions.

hash-style (`# @path[{rel}]`):
`.py` `.sh` `.bash` `.zsh` `.yaml` `.yml` `.toml` `.ini` `.cfg` `.rb` `.php` `.pl` `.r` `.tf` `.hcl` `.env` `Makefile` `Dockerfile` and more.

slash-style (`// @path[{rel}]`):
`.js` `.ts` `.jsx` `.tsx` `.go` `.rs` `.swift` `.cs` `.java` `.kt` `.scala` `.c` `.cpp` `.h` `.dart` `.proto` and more.

dash-style (`-- @path[{rel}]`):
`.sql` `.lua` `.hs` `.elm` `.vhd` `.vhdl` `.ada` and more.

HTML-style (`<!-- @path[{rel}] -->`):
`.html` `.xml` `.svg` `.md` `.markdown` and more.

block-style (`/* @path[{rel}] */`):
`.css` `.scss` `.sass` `.less` and more.

semicolon-style (`; @path[{rel}]`):
`.asm` `.s` `.nasm` and more.

## Installation

add to your `.pre-commit-config.yaml`, then run `pre-commit install`.

apply to all supported files in the repository:

```yaml
repos:
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
```

limit to specific directories with a `files` pattern:

```yaml
repos:
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
        files: ^(src|tests|scripts)/
```

exclude generated or vendored paths:

```yaml
repos:
  - repo: https://github.com/D7x7z49/fix-headers-hook
    rev: v0.1.0
    hooks:
      - id: fix-headers
        exclude: ^(vendor|generated|\.venv)/
```

## Safety and Scoping

- the hook only touches files whose extensions it recognizes. unsupported files are silently skipped.
- directories in `.gitignore` and common ignore paths (`.venv`, `node_modules`, `build`, `dist` ...) are never touched.
- shebang lines are preserved.
- run `pre-commit run fix-headers --all-files` to preview what would change before committing.
- if unsure, start with a narrow `files` pattern and widen gradually.

## Usage

once installed, the hook runs automatically on staged files during `git commit`.

to preview changes without committing:

```bash
pre-commit run fix-headers --all-files
```

to run the tool directly (outside pre-commit):

```bash
fix-headers src/ --dry-run    # preview
fix-headers src/              # apply
```

## How It Works

1. for each supported file, the tool computes its relative path from the project root
2. if the file has a shebang line, the header is inserted after it
3. a header is found by its `@path[...]` marker, so a moved file is rewritten in place
4. legacy headers without the marker are migrated on the first run
5. otherwise, the header is added

example: a file at `src/utils/helper.py` gets the header `# @path[src/utils/helper.py]`.

## Header Format

headers wrap the relative path in a `@path[...]` marker:

```text
# @path[src/utils/helper.py]
<!-- @path[README.md] -->
```

the marker gives the path an explicit start and end. the tool can then find a
header by shape instead of by value, so a renamed or moved file has its header
replaced rather than duplicated.

before v0.3.0 headers were bare paths, for example `# src/utils/helper.py`.
on the first run the hook migrates these in place. a bare first-line comment is
only treated as a header when it is a single token ending in a supported file
suffix, so ordinary comments are left alone.

## Development

see `make help` for all available targets.

quick start:

```bash
make install          # sync dependencies
make all              # lint + typecheck + test
make hook-test        # run all pre-commit hooks on all files
make self-test        # dry-run fix-headers on own source
```

development dependencies are declared in `pyproject.toml` under the `dev` extras group. Python version is pinned in `.python-version`.

## License

MIT license — see `LICENSE`.
