# docutil – Project Charter
Enterprise Documentation Automation Toolkit

---

## 1. Project Overview

**Project Name:** docutil  
**Owner:** Richie Garafola  
**Type:** Internal Engineering Tooling / Automation  
**Start Date:** 2026-02-13  
**Status:** Active  

### Purpose

docutil provides a deterministic, enterprise‑grade command‑line toolkit for converting, inspecting, and managing documentation assets including:

- DOCX ↔ Markdown
- Markdown → DOCX
- Batch operations
- Metadata inspection
- Project scaffolding

The goal is to standardize documentation workflows, eliminate manual formatting work, and enable automation across engineering, consulting, and GovCon environments.

---

## 2. Problem Statement

Engineering and consulting teams frequently:

• manually convert documents  
• maintain inconsistent formatting  
• perform repetitive transformations  
• lack reproducible pipelines  
• rely on GUI tools that cannot be automated  

This causes:

• wasted time  
• formatting errors  
• version control issues  
• poor CI/CD compatibility  

---

## 3. Objectives

### Primary Objectives

- Provide deterministic CLI utilities
- Enable scriptable batch conversions
- Support CI/CD automation
- Maintain zero external runtime dependencies (except Pandoc)
- Ensure professional output formatting

### Success Criteria

- 100% CLI coverage with tests
- CI pipeline passes on every commit
- Conversions are reproducible
- No manual steps required for standard workflows
- Clear documentation (README + USERGUIDE)

---

## 4. Scope

### In Scope

- DOCX → Markdown (GFM)
- Markdown → DOCX
- Batch conversions
- DOCX metadata inspection
- Project scaffolding
- CLI tooling
- Logging + progress bars
- Unit tests + CI
- Documentation standards

### Out of Scope

- GUI application
- Cloud hosting
- Real‑time collaboration tools
- Complex document editing features
- External LaTeX/PDF engines

---

## 5. Stakeholders

| Role | Responsibility |
|------|----------------|
| Project Owner | Architecture, development |
| Engineers | Usage + feedback |
| CI/CD Systems | Automated validation |
| Documentation Authors | Primary end users |

---

## 6. Deliverables

### Code Deliverables

- src/docutil package
- CLI interface
- Conversion modules
- Tests suite
- CI configuration

### Documentation Deliverables

- README.md
- USERGUIDE.md
- Technical Design
- Test Plan
- Project Charter
- Runbooks (future)

---

## 7. Risks & Mitigation

| Risk | Impact | Mitigation |
|--------|-----------|------------|
| Pandoc not installed | Conversion failure | doctor command |
| Large batch jobs | Slow runtime | parallel workers |
| Output overwrite errors | Data loss | --force flag |
| CI log noise | Reduced clarity | disable progress bars |

---

## 8. Constraints

- Python ≥ 3.10
- Local Pandoc installation required
- CLI-first design (no GUI)
- Minimal dependencies

---

## 9. Assumptions

- Engineers prefer CLI tools
- Pandoc remains stable
- Markdown (GFM) is the standard output
- Most workflows are file‑based and automatable

---

## 10. Timeline (High Level)

| Phase | Duration |
|-----------|-----------|
| Core CLI | 1 week |
| Conversions | 1 week |
| Batch + Logging | 1 week |
| Tests + CI | 1 week |
| Documentation | Ongoing |

---

## 11. Acceptance Criteria

The project is considered complete when:

✔ All commands pass tests  
✔ CI is green  
✔ README + USERGUIDE published  
✔ Conversions validated on real documents  
✔ Tool usable without manual intervention  

---

## 12. Approval

| Role | Name | Date |
|---------|----------|-----------|
| Owner | Richie Garafola | __________ |
| Reviewer | __________ | __________ |

---

End of Charter
