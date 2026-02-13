# Risk Register
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

This Risk Register identifies, tracks, and mitigates risks associated with the
development, deployment, and maintenance of the **docutil** toolkit.

The goal is to:

• Reduce operational surprises  
• Maintain deterministic behavior  
• Protect CI/CD stability  
• Ensure enterprise reliability  
• Support long‑term maintainability  

---

## Risk Scoring Model

| Score | Probability | Impact |
|-------|-------------|----------|
| 1 | Rare | Minimal |
| 2 | Unlikely | Low |
| 3 | Possible | Medium |
| 4 | Likely | High |
| 5 | Almost Certain | Critical |

Risk Score = Probability × Impact

| Score Range | Level |
|--------------|-----------|
| 1–5 | Low |
| 6–10 | Medium |
| 11–15 | High |
| 16–25 | Critical |

---

## Active Risks

| ID | Risk | Category | Prob | Impact | Score | Level | Mitigation | Owner | Status |
|----|-------|-----------|---------|----------|----------|-------------|--------------|----------|-----------|
| R-01 | Pandoc not installed on user system | Dependency | 4 | 4 | 16 | Critical | `docutil doctor` check + clear install instructions | Eng | Mitigated |
| R-02 | PDF engine requires LaTeX (external) | Dependency | 3 | 4 | 12 | High | Remove feature or optional install only | Eng | Accepted |
| R-03 | Breaking changes in Pandoc versions | Compatibility | 3 | 4 | 12 | High | Version enforcement + minimum checks | Eng | Mitigated |
| R-04 | Batch conversion on large repos is slow | Performance | 3 | 3 | 9 | Medium | Parallel workers + progress bars | Eng | Mitigated |
| R-05 | Accidental overwrite of user files | Data Loss | 2 | 5 | 10 | Medium | Default safe writes + `--force` required | Eng | Mitigated |
| R-06 | CLI usability confusion | UX | 3 | 2 | 6 | Medium | USERGUIDE + examples + help text | Eng | Active |
| R-07 | Poor test coverage leading to regressions | Quality | 3 | 4 | 12 | High | pytest suite + CI | Eng | Mitigated |
| R-08 | Cross‑platform path handling issues | Platform | 2 | 3 | 6 | Medium | pathlib usage everywhere | Eng | Mitigated |
| R-09 | Logging too verbose in CI | Operational | 2 | 2 | 4 | Low | progress disabled in non‑TTY + log levels | Eng | Mitigated |
| R-10 | Optional dependencies missing at runtime | Dependency | 3 | 3 | 9 | Medium | Clear feature groups + doctor checks | Eng | Active |

---

## Risk Categories

### Technical
• Dependency failures  
• Toolchain incompatibility  
• OS differences  

### Operational
• Incorrect user invocation  
• Missing binaries  
• Performance degradation  

### Process
• Insufficient testing  
• Poor documentation  
• Lack of onboarding guidance  

---

## Mitigation Strategy

### Preventive Controls
• `docutil doctor` diagnostics  
• Strict validation  
• Safe defaults  
• Idempotent operations  
• Automated tests  
• CI linting and type checks  

### Detective Controls
• Structured logging  
• Batch progress monitoring  
• Explicit exit codes  

### Corrective Controls
• Rollback capability (no destructive writes)  
• Quick reinstall steps  
• Clear troubleshooting guide  

---

## Review Cadence

| Frequency | Action |
|-------------|-----------|
| Every release | Reassess risks |
| Quarterly | Update probabilities |
| Major feature | Add new risks |
| Post‑incident | Root cause + new mitigation |

---

## Future Risk Candidates

• Add GUI front-end (complexity risk)  
• Cloud deployment packaging  
• Plugin ecosystem support  
• Large binary handling (multi‑GB PDFs)  
• Security scanning for document content  

---

## Acceptance Criteria

This register is considered effective when:

✓ No critical risks remain unmanaged  
✓ All high risks have mitigation plans  
✓ Tests prevent regressions  
✓ Users can self‑diagnose environment issues  

---

## Approval

| Role | Name | Signature | Date |
|--------|---------|--------------|--------|
| Project Lead | Richie Garafola |  |  |
| Reviewer |  |  |  |

---

**End of Document**
