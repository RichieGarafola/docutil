# Training Plan
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

## 1. Purpose

This Training Plan defines how users, engineers, and administrators will be
onboarded to effectively use and support the **docutil** toolkit.

Objectives:

• Reduce onboarding time  
• Enable self-service usage  
• Minimize support burden  
• Ensure safe operational practices  
• Standardize usage across teams  

---

## 2. Audience

| Role | Description | Training Depth |
|---------|------------------------------|----------------|
| End Users | Writers, analysts, PMs | Basic |
| Engineers | Developers integrating CLI | Intermediate |
| DevOps | CI/CD maintainers | Advanced |
| Maintainers | Project owners | Expert |

---

## 3. Training Goals

After training, participants should be able to:

✓ Install docutil and Pandoc  
✓ Run conversions confidently  
✓ Perform batch operations  
✓ Interpret logs and errors  
✓ Use safe defaults (--dry-run / --force)  
✓ Run diagnostics (`docutil doctor`)  
✓ Integrate into CI pipelines  
✓ Scaffold new projects  

---

## 4. Training Modules

### Module 1 — Overview (15 min)
• What is docutil  
• Supported formats  
• Design principles  
• CLI-first philosophy  

---

### Module 2 — Installation (15 min)

Hands-on:

```bash
conda create -n docutil python=3.11
conda activate docutil
conda install -c conda-forge pandoc
pip install docutil
docutil doctor
```

---

### Module 3 — Basic Usage (30 min)

Commands:

```bash
docutil docx2md report.docx
docutil md2docx notes.md
```

Concepts:
• deterministic output  
• safe writes  
• readable logs  

---

### Module 4 — Batch Operations (30 min)

```bash
docutil batch docx2md ./docs --recursive
docutil batch md2docx ./notes --dry-run
docutil batch docx2md ./docs --workers 4
```

Concepts:
• recursion  
• parallel workers  
• progress bars  
• dry-run safety  

---

### Module 5 — Diagnostics & Troubleshooting (20 min)

```bash
docutil doctor
docutil --verbose docx2md file.docx
```

Common issues:
• Pandoc missing  
• wrong file suffix  
• permission errors  

---

### Module 6 — CI/CD Integration (20 min)

Example:

```bash
pytest
docutil doctor
docutil batch docx2md ./docs --dry-run
```

Concepts:
• scripting  
• automation  
• deterministic builds  

---

### Module 7 — Project Scaffolding (10 min)

```bash
docutil scaffold project MyDocs ./workspace
```

Concepts:
• standard structure  
• safe regeneration  

---

## 5. Delivery Methods

| Method | Use Case |
|-------------|---------------------------|
| Live demo | Team onboarding |
| Recorded video | Async learning |
| Hands-on lab | Practical skill building |
| Documentation | Reference |
| USERGUIDE.md | Self-service |

---

## 6. Materials

Provided:

• README.md  
• USERGUIDE.md  
• Technical Design doc  
• Test Plan  
• Example files  
• CLI help (`--help`)  

Optional:

• Internal wiki  
• Cheat sheet  
• Recorded walkthrough  

---

## 7. Lab Exercises

### Exercise 1
Convert 5 DOCX files to Markdown.

### Exercise 2
Batch convert folder recursively.

### Exercise 3
Simulate overwrite protection and use --force.

### Exercise 4
Run doctor on a fresh environment.

### Exercise 5
Integrate into a simple CI job.

---

## 8. Success Criteria

Training is successful when:

✓ Users install without help  
✓ Users perform conversions independently  
✓ Support requests decrease  
✓ CI integration works reliably  
✓ No accidental overwrites reported  

---

## 9. Maintenance

| Frequency | Action |
|--------------|-------------|
| Each release | Update screenshots/examples |
| Quarterly | Refresh walkthrough |
| Major feature | Add new module |

---

## 10. Risks & Mitigation

| Risk | Mitigation |
|------------|---------------------------|
| Users skip docs | provide quick start |
| Confusion about Pandoc | doctor command |
| Unsafe overwrites | safe defaults |
| Feature creep | keep CLI simple |

---

## 11. Approval

| Role | Name | Signature | Date |
|---------|---------|-----------|--------|
| Project Lead | Richie Garafola |  |  |
| Trainer |  |  |  |

---

**End of Document**
