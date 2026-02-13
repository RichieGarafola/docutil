# Deployment Plan
## docutil — Enterprise Document Automation Toolkit

---

## Document Control

| Field | Value |
|-------|--------|
| Project | docutil |
| Owner | Richie Garafola |
| Version | 1.0 |
| Last Updated | 2026-02-13 |
| Status | Active |

---

## Purpose

This document defines the **deployment strategy, procedures, and rollback plan**
for releasing the **docutil** toolkit to users and environments.

Goals:

• Deterministic installs  
• Zero-downtime upgrades  
• Minimal external dependencies  
• Reproducible environments  
• CI/CD friendly packaging  

---

## Scope

### In Scope
• Python package distribution  
• CLI installation  
• Conda + pip environments  
• CI/CD integration  
• Version releases  
• Testing and validation  
• Rollback strategy  

### Out of Scope
• GUI hosting  
• Cloud infrastructure  
• External PDF engines (LaTeX, MiKTeX)  

---

## Deployment Architecture

User environments:

• Local developer machines  
• Conda virtual environments  
• CI pipelines (GitHub Actions / Azure DevOps)  
• Air‑gapped / enterprise networks  

Deployment model:

CLI → Python package → Pandoc dependency → File system operations

No servers or persistent services required.

---

## Environment Requirements

### Runtime
• Python ≥ 3.10  
• Pandoc installed (Conda recommended)  

### Optional
• python-docx (DOCX inspection)  
• pymupdf (PDF extraction)  

### Recommended
• Conda or venv isolation  

---

## Installation Procedure

### Step 1 — Create Environment

```bash
conda create -n docutil python=3.11 -y
conda activate docutil
```

### Step 2 — Install Pandoc

```bash
conda install -c conda-forge pandoc -y
```

### Step 3 — Install docutil

Editable (development):

```bash
pip install -e .
```

Production:

```bash
pip install docutil
```

### Step 4 — Verify

```bash
docutil doctor
docutil version
```

Expected:
• Pandoc detected
• No missing dependencies

---

## Release Strategy

### Versioning

Semantic Versioning:

MAJOR.MINOR.PATCH

| Type | Meaning |
|--------|------------|
| PATCH | bug fixes |
| MINOR | new features |
| MAJOR | breaking changes |

---

### Release Workflow

1. Run tests
2. Lint & type check
3. Update version
4. Tag release
5. Build package
6. Publish
7. Smoke test install

Commands:

```bash
pytest
ruff check .
mypy .
python -m build
```

---

## CI/CD Deployment Flow

Pipeline Steps:

1. Checkout code
2. Install dependencies
3. Install Pandoc
4. Run tests
5. Run CLI smoke tests
6. Build wheel
7. Publish artifact

Example:

```bash
docutil version
docutil doctor
docutil batch docx2md ./tests/data --dry-run
```

---

## Validation Checklist

Before release:

✓ All tests pass  
✓ CLI commands verified  
✓ doctor clean  
✓ Batch tested on sample repo  
✓ Documentation updated  

---

## Rollback Plan

If release fails:

1. Revert tag
2. Reinstall prior version

```bash
pip install docutil==PREVIOUS_VERSION
```

3. Communicate issue

Because docutil is stateless and file-based:
• No migrations required
• No database recovery required

Rollback is immediate and safe.

---

## Deployment Risks & Mitigation

| Risk | Mitigation |
|---------|----------------|
| Missing Pandoc | doctor command |
| OS path issues | pathlib usage |
| Large batches slow | parallel + progress |
| Accidental overwrite | --force required |
| External PDF engine issues | feature disabled |

---

## Operational Support

### Logs
• INFO default
• DEBUG via --verbose
• Optional file logging

### Diagnostics

```bash
docutil doctor
```

### Common Issues

| Problem | Solution |
|------------|--------------|
| Pandoc not found | conda install pandoc |
| Slow conversion | use --workers |
| Missing features | install optional extras |

---

## Maintenance Plan

| Frequency | Action |
|--------------|------------|
| Each release | run full test suite |
| Quarterly | dependency upgrades |
| Annually | major version review |

---

## Approval

| Role | Name | Signature | Date |
|---------|---------|-----------|--------|
| Project Lead | Richie Garafola |  |  |
| Reviewer |  |  |  |

---

**End of Document**
