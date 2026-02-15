# Getting Started

This guide walks you through installing, validating, and running
**docutil** in both production and development environments.

------------------------------------------------------------------------

# Installation

## Option A --- Install from PyPI (Recommended for Users)

``` bash
pip install docutil
```

After installation:

``` bash
docutil version
```

------------------------------------------------------------------------

# Optional Extras

Some features require optional dependencies.

## DOCX Metadata Inspection

``` bash
pip install "docutil[docx]"
```

Enables:

``` bash
docutil inspect docx file.docx
```

------------------------------------------------------------------------

# Development Installation

## 1️⃣ Clone Repository

``` bash
git clone https://github.com/RichieGarafola/docutil
cd docutil
```

------------------------------------------------------------------------

## 2️⃣ Create Virtual Environment (Recommended)

### Conda (recommended on Windows)

``` bash
conda create -n docutil python=3.11
conda activate docutil
```

### Or venv

``` bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

------------------------------------------------------------------------

## 3️⃣ Install in Editable Mode

``` bash
pip install -e ".[dev]"
```

Installs:

-   Testing dependencies
-   Ruff (lint/format)
-   MyPy (static typing)
-   Pytest
-   Pre-commit hooks

------------------------------------------------------------------------

# Verify Environment

``` bash
docutil doctor
```

Expected checks:

-   Python version
-   Pandoc availability
-   Write permissions
-   PATH resolution

If Pandoc is missing:

``` bash
conda install -c conda-forge pandoc
```

or download from:

https://pandoc.org/installing.html

------------------------------------------------------------------------

# Convert a File

## DOCX → Markdown

``` bash
docutil docx2md file.docx
```

Output:

    file.md

------------------------------------------------------------------------

## Markdown → DOCX

``` bash
docutil md2docx file.md
```

Output:

    file.docx

------------------------------------------------------------------------

# Deterministic Versioning

``` bash
docutil docx2md file.docx --versioned
```

Example output:

    file_2026-02-14_v1.md
    file_2026-02-14_v2.md

Ensures:

-   No silent overwrites
-   Clear traceability
-   Daily version tracking

------------------------------------------------------------------------

# Batch Conversion

``` bash
docutil batch docx2md ./docs
```

Recursive:

``` bash
docutil batch docx2md ./docs --recursive
```

Parallel:

``` bash
docutil batch docx2md ./docs --workers 4
```

Preview without writing:

``` bash
docutil batch docx2md ./docs --dry-run
```

------------------------------------------------------------------------

# Run Tests (Development)

``` bash
pytest -q
```

------------------------------------------------------------------------

# Lint & Type Check (Development)

``` bash
ruff check .
ruff format .
mypy src
```

------------------------------------------------------------------------

# Build Documentation Site

``` bash
pip install mkdocs-material
mkdocs serve
```

Visit:

http://127.0.0.1:8000

------------------------------------------------------------------------

Maintained by Richie Garafola\
MIT License
