# Changelog

All notable changes to **docutil** will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/).

------------------------------------------------------------------------

## \[Unreleased\]

### Added

-   Future enhancements under active development.

------------------------------------------------------------------------

## \[1.0.0\] - 2026-02-15

### Added

-   DOCX → Markdown conversion
-   Markdown → DOCX conversion
-   Batch conversion engine with:
    -   Recursive scanning
    -   Parallel workers
    -   Progress bars (TTY-aware)
    -   Dry-run mode
    -   Output folder support
-   Deterministic date + per-day version suffixing system
    (`--versioned`)
-   Environment diagnostics (`docutil doctor`)
-   DOCX metadata inspection (`docutil inspect docx`)
-   Project scaffolding system
-   Semantic version bump command (`docutil bump-version`)
-   Strict typing with MyPy enforcement
-   Ruff linting + formatting enforcement
-   Pytest coverage across CLI + batch engine

### Changed

-   Refactored batch engine for improved API clarity
-   Improved CLI typing for MyPy compatibility
-   Hardened error handling and overwrite logic

### Fixed

-   Tuple unpacking issue in CLI batch mode
-   Ruff formatting inconsistencies
-   Versioned output edge cases

------------------------------------------------------------------------

## Versioning Policy

-   **MAJOR**: Breaking changes
-   **MINOR**: New features (backwards compatible)
-   **PATCH**: Bug fixes and internal improvements

------------------------------------------------------------------------

## Release Process

1.  Ensure all tests pass (`pytest -q`)

2.  Ensure lint and type checks pass (`ruff check .`, `mypy src`)

3.  Bump version:

    ``` bash
    docutil bump-version minor
    ```

4.  Update CHANGELOG.md

5.  Commit and tag release

6.  Publish to PyPI

------------------------------------------------------------------------

© Richie Garafola
