
# Contributing to docutil

Thank you for your interest in contributing to **docutil**.

This project follows enterprise-grade development standards including:
- Strict typing (MyPy)
- Automated linting & formatting (Ruff)
- Automated testing (Pytest)
- Pre-commit enforcement
- CI validation (GitHub Actions)

---

## Development Philosophy

docutil prioritizes:

- Deterministic behavior
- Explicit over implicit design
- Zero hidden side effects
- CI/CD friendliness
- Clean, predictable CLI UX
- Production-grade documentation

All contributions must maintain these principles.

---

## Development Setup

Clone the repository:

```bash
git clone https://github.com/RichieGarafola/docutil
cd docutil
```

Install in editable development mode:

```bash
pip install -e ".[dev]"
```

Verify tooling:

```bash
ruff check .
mypy src
pytest -q
```

All checks must pass before submitting a PR.

---

## Branching Strategy

Use feature branches:

```
feature/<short-description>
fix/<short-description>
docs/<short-description>
refactor/<short-description>
```

Never commit directly to `main`.

---

## Code Standards

### Formatting
Ruff handles both linting and formatting.

```bash
ruff check . --fix
ruff format .
```

### Typing
All public functions must be type annotated.

```bash
mypy src
```

### Testing
All new features must include tests.

```bash
pytest -q
```

Test expectations:
- Deterministic behavior
- Edge cases covered
- No reliance on system state
- Fast execution

---

## Pull Request Requirements

Before submitting a PR:

- [ ] Ruff passes
- [ ] MyPy passes
- [ ] Pytest passes
- [ ] Documentation updated (if applicable)
- [ ] Changelog entry added (if applicable)

PRs should include:
- Clear description of change
- Motivation / reasoning
- Test coverage explanation

---

## Commit Message Style

Follow conventional commit style:

```
feat: add versioned batch output
fix: resolve mypy typing issue
docs: update CLI reference
refactor: simplify batch engine
```

---

## Reporting Issues

When filing a bug report include:

- Python version
- OS
- Pandoc version
- Command executed
- Full traceback
- Expected vs actual behavior

---

## Code of Conduct

Be respectful.
Be precise.
Be constructive.

We aim to build production-quality tooling.

---

## Maintainer Notes

The maintainer reserves the right to:

- Request refactors before merging
- Reject changes that introduce non-determinism
- Require test improvements
- Enforce documentation quality standards

---

Thank you for helping make docutil production-ready.
