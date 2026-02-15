
# docutil

Enterprise Document Utility Toolkit  
Built for deterministic, production-grade document workflows.

---

## Overview

**docutil** is a command-line toolkit designed for structured, repeatable,
and enterprise-safe document automation.

It provides:

- DOCX → Markdown conversion
- Markdown → DOCX conversion
- Parallel batch processing
- Deterministic date + version suffixing
- Environment diagnostics
- Metadata inspection
- Project scaffolding
- Semantic version bumping
- CI/CD compatibility

---

## Why docutil?

Traditional document tooling is often:

- Manual
- Non-deterministic
- Hard to automate
- Risky in CI/CD pipelines

`docutil` is designed with engineering principles in mind:

- Safe defaults
- Explicit flags
- No silent overwrites
- Clean logging
- Strong typing
- Test coverage
- Enterprise documentation standards

---

## Quick Start

### Convert a File

```bash
docutil docx2md input.docx
docutil md2docx input.md
```

### Use Versioned Output

```bash
docutil docx2md input.docx --versioned
```

Produces:

```
input_2026-02-15_v1.md
```

---

## Batch Processing

```bash
docutil batch docx2md ./docs --recursive --workers 4
```

Supports:

- Recursive scanning
- Parallel workers
- Output folder control
- Dry-run validation
- Versioned batch output

---

## Inspect Metadata

```bash
docutil inspect docx file.docx
docutil inspect docx file.docx --json
```

---

## Environment Diagnostics

```bash
docutil doctor
```

Validates:

- Python version
- Pandoc availability
- PATH resolution
- Write permissions

---

## Semantic Version Management

```bash
docutil bump-version patch
docutil bump-version minor
docutil bump-version major
```

Updates `pyproject.toml` automatically.

---

## Documentation Structure

This site includes:

- Getting Started Guide
- CLI Reference
- Versioning System Overview
- Architecture Documentation
- Contribution Guidelines
- Changelog

---

## Author

Richie Garafola  
Enterprise Automation & Document Engineering

---

© 2026 Richie Garafola
