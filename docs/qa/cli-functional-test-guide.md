# docutil CLI -- Full Functional Test Guide

This document provides a complete command-by-command validation
checklist for the `docutil` CLI.

Use this guide to:

-   Validate feature correctness
-   Confirm error handling
-   Verify optional dependencies
-   Confirm CI-safe behavior
-   Test edge cases
-   Validate overwrite protections

------------------------------------------------------------------------

# 🔷 GLOBAL OPTIONS

## 1️⃣ Verbose Logging

``` bash
docutil --verbose doctor
```

Expected: - DEBUG-level logs visible - No errors

------------------------------------------------------------------------

## 2️⃣ Log Output to File

``` bash
docutil --log-file cli.log doctor
```

Expected: - `cli.log` created - Structured logs written

------------------------------------------------------------------------

# 🔷 CORE COMMANDS

## 3️⃣ Environment Check

``` bash
docutil doctor
```

Expected: - Python version - Pandoc version - Write permissions - Pandoc
path

------------------------------------------------------------------------

## 4️⃣ Version

``` bash
docutil version
```

Expected: - Prints `__version__`

------------------------------------------------------------------------

# 🔷 SINGLE FILE CONVERSIONS

## 5️⃣ DOCX → Markdown

``` bash
docutil docx2md test.docx
docutil docx2md test.docx custom.md
docutil docx2md test.docx custom.md --force
```

Failure test (no force):

``` bash
docutil docx2md test.docx custom.md
```

------------------------------------------------------------------------

## 6️⃣ Markdown → DOCX

``` bash
docutil md2docx test.md
docutil md2docx test.md custom.docx
docutil md2docx test.md custom.docx --force
```

------------------------------------------------------------------------

# 🔷 BATCH MODE

Create:

    batch_test/
        a.docx
        b.docx
        nested/
            c.docx

### Basic

``` bash
docutil batch docx2md ./batch_test
```

### Recursive

``` bash
docutil batch docx2md ./batch_test --recursive
```

### Dry Run

``` bash
docutil batch docx2md ./batch_test --dry-run
```

### Output Folder

``` bash
docutil batch docx2md ./batch_test --out-folder ./converted
```

### Workers

``` bash
docutil batch docx2md ./batch_test --workers 4
```

### Disable Progress

``` bash
docutil batch docx2md ./batch_test --no-progress
```

------------------------------------------------------------------------

# 🔷 INSPECT

Requires:

``` bash
pip install -e ".[docx]"
```

### Metadata

``` bash
docutil inspect docx test.docx
```

### JSON Output

``` bash
docutil inspect docx test.docx --json
```

------------------------------------------------------------------------

# 🔷 SCAFFOLD

``` bash
docutil scaffold project MyProject ./output
docutil scaffold project MyProject ./output --force
```

------------------------------------------------------------------------

# 🔷 FAILURE TESTS

Invalid mode:

``` bash
docutil batch invalid ./docs
```

Nonexistent file:

``` bash
docutil docx2md fake.docx
```

------------------------------------------------------------------------

# 🔷 Regression Checklist

  Feature            Status
  ------------------ --------
  Logging            ☐
  Doctor             ☐
  Version            ☐
  DOCX→MD            ☐
  MD→DOCX            ☐
  Batch              ☐
  Recursive          ☐
  Dry-run            ☐
  Workers            ☐
  Inspect            ☐
  JSON               ☐
  Scaffold           ☐
  Failure Handling   ☐

------------------------------------------------------------------------

Planned Enhancement: Auto-append date + version suffix:
`report_2026-02-14_v1.md`
