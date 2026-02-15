# CLI Reference

Complete command-line reference for **docutil**.

------------------------------------------------------------------------

## Global Options

These options apply to all commands and must be placed before the
subcommand.

### `--verbose`

Enable debug-level logging.

``` bash
docutil --verbose doctor
```

### `--log-file PATH`

Write structured logs to a file.

``` bash
docutil --log-file cli.log doctor
```

------------------------------------------------------------------------

## Core Commands

### `doctor`

Validate local environment configuration.

Checks: - Python version - Pandoc availability - Write permissions -
PATH resolution

``` bash
docutil doctor
```

------------------------------------------------------------------------

### `version`

Print the installed docutil version.

``` bash
docutil version
```

------------------------------------------------------------------------

## Single File Conversion

### `docx2md`

Convert a DOCX file to Markdown.

``` bash
docutil docx2md input.docx
docutil docx2md input.docx output.md
docutil docx2md input.docx output.md --force
docutil docx2md input.docx output.md --versioned
```

Options:

-   `--force` --- overwrite existing output
-   `--versioned` --- append date + per-day version suffix

------------------------------------------------------------------------

### `md2docx`

Convert a Markdown file to DOCX.

``` bash
docutil md2docx input.md
docutil md2docx input.md output.docx
docutil md2docx input.md output.docx --versioned
```

Options:

-   `--force` --- overwrite existing output
-   `--versioned` --- append date + per-day version suffix

------------------------------------------------------------------------

## Batch Conversion

### `batch`

Batch convert files inside a directory.

``` bash
docutil batch docx2md ./docs
docutil batch docx2md ./docs --recursive
docutil batch docx2md ./docs --out-folder ./converted
docutil batch docx2md ./docs --workers 4
docutil batch docx2md ./docs --versioned
```

Arguments:

-   `mode` --- `docx2md` or `md2docx`
-   `folder` --- input directory

Options:

-   `--recursive` --- include subdirectories
-   `--dry-run` --- preview changes only
-   `--force` --- overwrite outputs
-   `--versioned` --- apply date+version suffix
-   `--out-folder` --- output directory
-   `--no-progress` --- disable progress bar
-   `--workers N` --- parallel worker count

------------------------------------------------------------------------

## Inspect

### `inspect docx`

Inspect DOCX metadata (requires optional docx dependency).

``` bash
docutil inspect docx file.docx
docutil inspect docx file.docx --json
```

Options:

-   `--json` --- output metadata as JSON

------------------------------------------------------------------------

## Scaffold

### `scaffold project`

Generate a project template structure.

``` bash
docutil scaffold project MyProject ./output
docutil scaffold project MyProject ./output --force
```

Options:

-   `--force` --- overwrite existing directory

------------------------------------------------------------------------

## Version Management

### `bump-version`

Bump semantic version in `pyproject.toml`.

``` bash
docutil bump-version patch
docutil bump-version minor
docutil bump-version major
```

------------------------------------------------------------------------

## Exit Codes

  Code   Meaning
  ------ ------------------------------------------------------
  0      Success
  1      User error (invalid arguments, overwrite protection)
  \>1    Runtime or environment failure

------------------------------------------------------------------------

## Design Guarantees

-   Deterministic behavior
-   Explicit flags (no hidden side effects)
-   Safe defaults
-   CI/CD compatible
-   Structured logging
-   Type-safe interfaces
