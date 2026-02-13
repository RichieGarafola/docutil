# docutil — Project Timeline

**Project:** docutil (Enterprise Document Automation Toolkit)  
**Owner:** Richie Garafola  
**Version:** 1.0  
**Document Type:** Delivery Timeline / Roadmap  
**Audience:** Engineers, Maintainers, Stakeholders  

---

## 1. Overview

This timeline outlines phased delivery of the **docutil** toolkit, focusing on:

• Stability first  
• CLI-first usability  
• Deterministic behavior  
• Enterprise readiness  
• CI/CD + testing maturity  
• Low operational friction  

The roadmap is intentionally **incremental** to ensure each phase ships usable value.

---

## 2. Delivery Phases

| Phase | Name | Duration | Outcome |
|-------|--------|-----------|-----------|
| 1 | Core CLI & Conversions | Week 1 | Working DOCX ↔ MD conversions |
| 2 | Batch + Logging | Week 2 | Production-safe automation |
| 3 | Testing + CI | Week 3 | Reliability + regression safety |
| 4 | Documentation Suite | Week 4 | Enterprise-grade docs |
| 5 | Diagnostics + Hardening | Week 5 | `doctor`, error clarity |
| 6 | Performance Enhancements | Week 6 | Parallel batch + polish |
| 7 | Future Enhancements | Backlog | Optional features |

---

## 3. Phase Details

### Phase 1 — Core CLI & Conversions
**Goal:** Minimum viable toolkit

Deliverables:
- docx2md
- md2docx
- pandoc detection
- structured logging
- packaging (pyproject.toml)

Success Criteria:
- Deterministic conversions
- CLI installs via pip
- No external runtime dependencies beyond Pandoc

---

### Phase 2 — Batch + Logging
**Goal:** Automation readiness

Deliverables:
- batch conversion
- progress bars (tqdm)
- --dry-run
- --force
- safe overwrite logic
- improved logs

Success Criteria:
- Handles 100+ files reliably
- Clear CLI output
- CI-friendly behavior

---

### Phase 3 — Testing + CI
**Goal:** Production reliability

Deliverables:
- pytest suite
- smoke tests
- batch tests
- conversion tests
- GitHub Actions CI
- lint + type checks

Success Criteria:
- All tests green in CI
- No regressions
- Reproducible builds

---

### Phase 4 — Documentation Suite
**Goal:** Enterprise adoption

Deliverables:
- README.md
- USERGUIDE.md
- Technical Design
- Test Plan
- Project Charter
- Timeline (this document)

Success Criteria:
- New engineer onboarding < 15 minutes
- All commands documented
- GovCon-friendly format

---

### Phase 5 — Diagnostics + Hardening
**Goal:** Operational safety

Deliverables:
- docutil doctor
- pandoc version checks
- environment validation
- clearer error messages
- logging improvements

Success Criteria:
- Easy troubleshooting
- Reduced support overhead

---

### Phase 6 — Performance Enhancements
**Goal:** Scalability

Deliverables:
- parallel batch (--workers)
- optimized I/O
- large-folder support
- performance benchmarks

Success Criteria:
- 3–5x faster batch processing
- Stable memory usage

---

### Phase 7 — Backlog / Optional
Future ideas (non-blocking):

- GUI (Streamlit or Textual)
- Markdown linting
- PDF export (optional engines)
- template libraries
- metadata enrichment
- plugin architecture

---

## 4. Visual Timeline

```
Week:   1   2   3   4   5   6
        |---|---|---|---|---|
Core    ████
Batch       ████
Testing         ████
Docs               ████
Doctor                  ████
Perf                        ████
```

---

## 5. Risks & Mitigation

| Risk | Impact | Mitigation |
|---------|-----------|-------------|
| Pandoc not installed | Conversions fail | `doctor` command |
| Large file batches | Slow runtime | parallel processing |
| Dependency drift | Build failures | pinned versions |
| Poor onboarding | Low adoption | strong docs |

---

## 6. Acceptance Criteria

The project is considered **production-ready** when:

✓ Conversions stable  
✓ Batch safe + fast  
✓ Tests passing  
✓ CI green  
✓ Docs complete  
✓ Diagnostics included  

---

## 7. Change Log

| Date | Change |
|--------|------------|
| Initial | Timeline created |

---

**End of Document**
