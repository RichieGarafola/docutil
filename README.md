
# docutil

**Enterprise‑grade document automation toolkit for deterministic DOCX and Markdown workflows.**

docutil is a lightweight, CLI‑first Python utility built for engineers, analysts, and automation teams who need **repeatable, scriptable, CI‑safe document processing**.

It provides reliable conversions and batch processing between:

• DOCX ↔ Markdown (GitHub Flavored Markdown)  
• Folder‑wide batch conversions  
• Project scaffolding  
• Metadata inspection  
• Environment diagnostics  

Designed specifically for **automation, consulting, and enterprise environments** where reproducibility and reliability matter more than GUIs.

---

# Table of Contents

- Overview
- Design Philosophy
- Features
- Architecture
- Installation
- Quick Start
- Command Reference
- Batch Workflows
- CI/CD Usage
- Testing
- Development
- Troubleshooting
- Roadmap

---

# Overview

docutil replaces manual document conversion tasks with deterministic, scriptable commands.

Typical use cases:

• Convert Word deliverables into Markdown for GitHub  
• Convert Markdown documentation back to DOCX for clients  
• Batch migrate entire repositories  
• Run document transformations inside CI pipelines  
• Standardize documentation workflows across teams  

---

# Design Philosophy

docutil intentionally avoids:

❌ GUIs  
❌ heavy runtime dependencies  
❌ OS‑specific installers  
❌ hidden side effects  
❌ non‑deterministic output  

Instead it prioritizes:

✅ CLI‑first  
✅ deterministic output  
✅ automation friendly  
✅ testability  
✅ CI safety  
✅ minimal dependencies  

If it can’t run in a headless CI environment, it doesn’t belong here.

---

# Features

## Conversions
• DOCX → Markdown (GFM)  
• Markdown → DOCX  
• Stable output formatting  
• No automatic line wrapping  
• ATX headings (# style)

## Batch Engine
• recursive scanning  
• dry‑run preview  
• progress bars (TTY aware)  
• parallel workers  
• safe overwrite control  
• out‑folder support  
• CI friendly logging  

## Tooling
• project scaffolding  
• metadata inspection  
• environment diagnostics (`doctor`)  
• structured logging  
• pytest test suite  
• type checking (mypy)  
• linting (ruff)

---

# Architecture

```
docutil/
│
├── cli.py                 # Typer CLI interface
├── conversions/           # Conversion engines
├── inspect/               # Metadata utilities
├── templates/             # Project scaffolding
├── doctor.py              # Environment diagnostics
├── logging_utils.py       # Centralized logging
└── tests/                 # Fast unit tests
```

### Core principles

• CLI is thin  
• business logic lives in modules  
• deterministic I/O  
• side effects explicit  
• easy to test  

---

# Installation

## 1. Install Pandoc (required for conversions)

Recommended:

```
conda install -c conda-forge pandoc
```

## 2. Install docutil

```
pip install -e .
```

## Optional (development)

```
pip install -e .[dev]
```

Includes:

• pytest  
• ruff  
• mypy  

---

# Quick Start

## Convert one file

DOCX → Markdown

```
docutil docx2md report.docx
```

Markdown → DOCX

```
docutil md2docx notes.md
```

---

## Batch convert a directory

```
docutil batch docx2md ./docs --recursive
```

---

## Preview changes only

```
docutil batch docx2md ./docs --dry-run
```

---

## Output to separate directory

```
docutil batch md2docx ./docs --out-folder ./out
```

---

## Parallel workers

```
docutil batch docx2md ./docs --workers 4
```

---

## Scaffold new project

```
docutil scaffold project MyProject .
```

---

## Environment check

```
docutil doctor
```

---

# Command Reference

```
docutil version
docutil doctor

docutil docx2md <file>
docutil md2docx <file>

docutil batch <mode> <folder>

docutil scaffold project <name> <dir>

docutil inspect docx <file>
```

---

# Batch Workflows

### Large repository migration

```
docutil batch docx2md docs --recursive --dry-run
docutil batch docx2md docs --recursive --workers 4
```

### Preserve originals

```
docutil batch md2docx docs --out-folder out
```

### CI friendly

```
docutil batch docx2md docs --recursive --no-progress
```

---

# CI/CD Usage

Example GitHub Actions step:

```
docutil batch docx2md docs --recursive --no-progress
```

No progress bars = clean logs.

---

# Testing

Run locally:

```
pytest -q
```

Tests are:

• fast (<1s)  
• Pandoc mocked  
• deterministic  

---

# Development

Lint:

```
ruff check .
```

Type check:

```
mypy src
```

---

# Troubleshooting

## Pandoc not found

```
conda install -c conda-forge pandoc
```

## Permission issues

```
docutil doctor
```

## Slow batch

Increase workers:

```
--workers 4
```

---

# Roadmap

Planned:

• richer batch summaries  
• optional integration tests  
• packaging for PyPI  
• additional inspection tools  

---

# License

Internal / Enterprise use
