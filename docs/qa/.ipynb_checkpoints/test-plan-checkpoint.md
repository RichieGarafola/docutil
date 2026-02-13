
# docutil Test Plan

## Document Purpose

This document defines the **testing strategy, scope, and quality gates** for the docutil project.

Audience:
• Engineers
• Maintainers
• QA reviewers
• CI/CD owners

Goals:
• ensure reliability
• prevent regressions
• maintain deterministic behavior
• keep tests fast and automation-friendly

---

# 1. Test Objectives

The testing approach must guarantee:

• conversions behave deterministically  
• CLI commands function correctly  
• batch operations are safe  
• failures are explicit and actionable  
• changes do not break CI environments  

Success criteria:

✔ All unit tests pass  
✔ Type checks pass  
✔ Lint checks pass  
✔ No interactive behavior  
✔ No environment-specific failures  

---

# 2. Scope

## In Scope

• conversion functions  
• batch engine behavior  
• CLI command routing  
• argument validation  
• logging behavior  
• dry-run safety  
• out-folder mapping  
• parallel execution correctness  
• environment diagnostics  

## Out of Scope

• Pandoc internal behavior  
• OS-specific rendering differences  
• GUI behavior (none by design)  
• network-based testing (none required)  

---

# 3. Test Strategy

docutil uses a **layered testing approach**:

| Layer | Purpose | Speed |
|--------|----------|----------|
| Unit | logic validation (mocked pandoc) | very fast |
| CLI | command wiring & smoke tests | fast |
| Integration (optional) | real pandoc conversions | slower |

Unit tests are the primary safety net.

---

# 4. Test Types

## 4.1 Unit Tests (Primary)

Framework: pytest

Characteristics:

• pandoc mocked  
• deterministic  
• sub-second runtime  
• no external dependencies  

### Examples

• validate file existence checks  
• validate suffix validation  
• verify pypandoc.convert_file called correctly  
• dry-run prevents conversion  
• force flag overwrites correctly  
• out-folder mapping preserves structure  
• workers do not duplicate or skip files  

---

## 4.2 CLI Smoke Tests

Framework: Typer CliRunner

Purpose:

Validate command wiring and exit codes.

### Examples

• docutil version returns 0  
• docutil doctor returns 0  
• invalid command returns non-zero  
• missing file returns non-zero  

---

## 4.3 Integration Tests (Optional)

Runs with real Pandoc installed.

Purpose:

Validate end-to-end conversions.

Characteristics:

• limited fixtures only  
• small files only  
• executed in CI separately  

Example:

• .md → .docx → .md roundtrip  

---

# 5. Test Coverage Targets

Recommended minimums:

• 90%+ core logic  
• 100% CLI coverage  
• 100% batch engine coverage  

Focus on behavior, not lines.

---

# 6. Test Structure

```
tests/
│
├── conftest.py
├── test_cli_smoke.py
├── test_batch.py
├── test_docx2md.py
├── test_md2docx.py
```

### Responsibilities

conftest.py  
• fixtures  

test_cli_smoke.py  
• CLI health checks  

test_batch.py  
• dry-run  
• recursion  
• workers  
• out-folder  

test_docx2md.py  
• validation + pandoc call  

test_md2docx.py  
• validation + pandoc call  

---

# 7. Test Data Guidelines

Rules:

• use minimal fixtures  
• avoid large files  
• avoid binary artifacts in repo  
• generate temporary files during tests  

Use tmp_path fixture for isolation.

---

# 8. Continuous Integration

Every commit must run:

pytest -q  
ruff check .  
mypy src  

Failures block merges.

Optional integration job:

• installs pandoc  
• runs small conversion tests  

---

# 9. Performance Requirements

Test suite goals:

• total runtime < 2 seconds  
• no network access  
• no large file I/O  

Fast tests encourage frequent execution.

---

# 10. Error Handling Verification

Tests must verify:

• FileNotFoundError raised  
• invalid suffix raises ValueError  
• pandoc missing raises RuntimeError  
• CLI returns non-zero exit code on failures  

Never silently fail.

---

# 11. Regression Policy

For every bug:

1. Write failing test  
2. Fix bug  
3. Verify test passes  
4. Merge  

No bug fixes without tests.

---

# 12. Release Criteria

Before tagging a release:

✔ All tests passing  
✔ Lint clean  
✔ Type check clean  
✔ Manual smoke test of CLI  
✔ doctor command validated  

---

# 13. Future Improvements

Potential enhancements:

• property-based testing (hypothesis)  
• parallel stress testing  
• Windows/macOS matrix CI  
• integration round-trip tests  

---

# 14. Conclusion

docutil prioritizes:

• fast tests  
• deterministic behavior  
• CI reliability  

This ensures the tool remains:

• safe to refactor  
• stable for automation  
• production ready  
