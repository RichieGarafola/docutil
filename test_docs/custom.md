# docutil

**Enterprise-grade document automation toolkit for engineers, analysts, and GovCon teams**

`docutil` provides reliable, deterministic, and scriptable conversions between:

- Microsoft Word (`.docx`)
- GitHub-Flavored Markdown (GFM)
- PDF reports

It is designed for:

- Technical documentation
- Proposal writing
- Compliance artifacts
- SOP automation
- Dashboard/report exports
- Batch processing of large document sets

Built on **Pandoc + Python**, with a clean CLI and reusable library functions.

------------------------------------------------------------------------

## Key Capabilities

✔ DOCX → Markdown (GitHub-ready)\
✔ Markdown → DOCX (client deliverables)\
✔ Markdown → PDF (executive reports)\
✔ Batch conversions across folders\
✔ DOCX metadata inspection\
✔ PDF text extraction (optional)\
✔ Project scaffolding templates\
✔ Scriptable + CI/CD friendly

------------------------------------------------------------------------

## Design Philosophy

`docutil` follows enterprise engineering best practices:

- Deterministic outputs
- Explicit error handling
- Structured logging
- Type-safe functions
- Path-first APIs
- CLI + importable modules
- No hidden side effects
- Works locally, in Docker, or CI pipelines

This is not a one-off script — it’s a **professional toolbelt**.

------------------------------------------------------------------------

## Installation

### 1. Install Pandoc (required)

### Conda (recommended)

    conda install -c conda-forge pandoc

### Verify

    pandoc --version

### 2. Install docutil

### Editable install (recommended for development)

pip install -e .

### With optional features

pip install -e ".\[docx,pdf,dev\]"

| Feature         | Dependency         |
|-----------------|--------------------|
| DOCX metadata   | python-docx        |
| PDF extraction  | PyMuPDF            |
| Testing/Linting | pytest, ruff, mypy |

### Quick Start

### Convert Word → Markdown

    docutil docx2md report.docx

### Convert Markdown → Word

    docutil md2docx README.md

### Convert Markdown → PDF

    docutil md2pdf report.md

### Batch convert folder

    docutil batch docx2md ./proposals --recursive

### Inspect metadata

    docutil inspect docx proposal.docx

### Extract PDF text

    docutil inspect pdf contract.pdf --out-text contract.txt

### Scaffold new project

    docutil scaffold project MyNewTool ./workspace

### Example Workflows

### Proposal modernization

    docutil batch docx2md ./legacy_proposals --recursive

Executive reporting

    docutil md2pdf weekly_report.md

### Compliance audit

    docutil inspect docx training_plan.docx

### Repo bootstrap

    docutil scaffold project BudgetAutomation ./projects

### Python API Usage

All tools are importable for automation pipelines:

    from docutil.conversions.docx_to_markdown import docx_to_markdown

    output = docx_to_markdown("proposal.docx")
    print(output)

Batch example:

    from docutil.conversions.batch import batch_convert
    from docutil.conversions.docx_to_markdown import docx_to_markdown

    batch_convert("./input", ".docx", docx_to_markdown, recursive=True)

### Project Structure

docutil/ ├── conversions/ ├── inspect/ ├── templates/ ├── cli.py ├── pandoc_utils.py └── logging_utils.py

Modules are organized by responsibility: \| Folder \| Purpose \| \| ----------- \| --------------------------- \| \| conversions \| File format conversions \| \| inspect \| Metadata + extraction tools \| \| templates \| Project scaffolding \| \| cli \| Command line interface \|

### Requirements

- Python 3.10+
- Pandoc
- (Optional) LaTeX engine for PDF output

### Windows PDF tip

Install MiKTeX if PDF export fails:

    https://miktex.org/

### Troubleshooting

### Pandoc not found

    RuntimeError: Pandoc is not installed

Fix:

    conda install -c conda-forge pandoc

### PDF conversion fails

Likely missing PDF engine.

Install:

- MiKTeX (Windows)
- TeX Live (Linux/macOS)

### Development

Run tests:

    pytest

Lint:

    ruff check .

Type check:

    mypy .

### Intended Audience

- Data engineers
- Analysts
- Technical writers
- Proposal teams
- GovCon/DoD environments
- Anyone converting Word ↔ Markdown ↔ PDF at scale

------------------------------------------------------------------------

------------------------------------------------------------------------

### Author

Richie Garafola Enterprise Analytics & Automation Created: 2026-02-13
