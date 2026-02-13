
# docutil User Guide

This guide focuses on **how to use docutil in real-world workflows**.

Unlike the README (engineer-focused architecture + design), this document is:

• task-oriented  
• example-driven  
• operational  
• suitable for analysts and day-to-day users  

If you just want to get work done quickly, start here.

---

# Table of Contents

- Quick Examples
- Single File Conversions
- Batch Processing
- Safe Operations (dry-run, force)
- Output Management
- Performance (parallel workers)
- CI / Automation Usage
- Project Scaffolding
- Metadata Inspection
- Doctor (Environment Checks)
- Common Workflows
- Troubleshooting
- Best Practices

---

# Quick Examples

## Convert one Word file to Markdown

```
docutil docx2md report.docx
```

Creates:
```
report.md
```

---

## Convert Markdown back to Word

```
docutil md2docx notes.md
```

Creates:
```
notes.docx
```

---

## Convert an entire folder

```
docutil batch docx2md ./docs --recursive
```

---

# Single File Conversions

## DOCX → Markdown

```
docutil docx2md input.docx
```

### Optional output file

```
docutil docx2md input.docx --out output.md
```

---

## Markdown → DOCX

```
docutil md2docx input.md
```

---

# Batch Processing

Batch mode is the most common usage in real projects.

Process all matching files inside a directory.

## Basic

```
docutil batch docx2md ./docs
```

---

## Recursive

```
docutil batch docx2md ./docs --recursive
```

Processes:

```
docs/**/*.docx
```

---

# Safe Operations

## Dry Run (preview only)

Shows what *would* happen without modifying anything.

```
docutil batch docx2md ./docs --dry-run
```

Recommended before large migrations.

---

## Force overwrite

Overwrite existing output files.

```
docutil batch docx2md ./docs --force
```

Use carefully.

---

# Output Management

## Write outputs to another folder

```
docutil batch md2docx ./docs --out-folder ./out
```

### Example

Input:
```
docs/a.md
docs/sub/b.md
```

Output:
```
out/a.docx
out/sub/b.docx
```

Folder structure is preserved automatically.

---

# Performance (Parallel Workers)

For large directories, use multiple workers.

```
docutil batch docx2md ./docs --workers 4
```

Guidelines:

• small sets (<20 files): default (1)  
• medium sets: 2–4 workers  
• large sets (100+ files): 4–8 workers  

---

# Progress Bars

By default progress bars show in terminals.

Disable for CI or clean logs:

```
docutil batch docx2md ./docs --no-progress
```

---

# CI / Automation Usage

docutil is designed for pipelines.

Example:

```
docutil batch docx2md docs --recursive --no-progress
```

Typical use cases:

• pre-commit hooks  
• nightly conversions  
• automated documentation builds  
• client deliverable packaging  

---

# Project Scaffolding

Create a clean documentation project structure.

```
docutil scaffold project MyProject .
```

Creates:

```
MyProject/
├── README.md
├── docs/
├── src/
├── tests/
└── .gitignore
```

---

# Metadata Inspection

Inspect document metadata.

```
docutil inspect docx file.docx
```

Useful for debugging or auditing files.

---

# Doctor (Environment Diagnostics)

If something fails, run:

```
docutil doctor
```

Checks:

• Python version  
• Pandoc availability  
• PATH  
• write permissions  

---

# Common Workflows

## Word → Markdown repository migration

```
docutil batch docx2md docs --recursive --dry-run
docutil batch docx2md docs --recursive
```

---

## Markdown → Client Word deliverables

```
docutil batch md2docx docs --out-folder deliverables --workers 4
```

---

## CI build

```
docutil batch docx2md docs --recursive --no-progress
```

---

# Troubleshooting

## Pandoc not found

Install:

```
conda install -c conda-forge pandoc
```

---

## Permission errors

Run:

```
docutil doctor
```

---

## Slow conversions

Increase workers:

```
--workers 4
```

---

# Best Practices

✔ Always dry-run first  
✔ Use out-folder to protect originals  
✔ Use parallel workers for large jobs  
✔ Disable progress in CI  
✔ Keep conversions deterministic  
✔ Commit only necessary generated files  

---

# Summary

docutil is optimized for:

• engineers  
• analysts  
• automation  
• CI/CD  
• enterprise reliability  

Use batch mode + automation to get the most value.
