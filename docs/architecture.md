# Architecture

## Overview

**docutil** is designed as a modular, deterministic, and
production-grade document automation toolkit.

The architecture follows a layered design:

    CLI Layer (Typer)
            ↓
    Application Layer (Conversion Orchestration)
            ↓
    Conversion Engines (Pandoc, python-docx)
            ↓
    Utilities (Logging, Versioning, Validation)

This separation ensures:

-   Clean dependency boundaries
-   High testability
-   CI/CD compatibility
-   Future extensibility

------------------------------------------------------------------------

## Core Components

### 1. CLI Layer (`cli.py`)

Built with **Typer**, the CLI provides:

-   Command routing
-   Input validation
-   Output safety controls
-   Logging configuration
-   Version bumping
-   Batch execution orchestration

The CLI is intentionally thin. All business logic lives below this
layer.

------------------------------------------------------------------------

### 2. Conversion Layer

Located under:

    src/docutil/conversions/

Contains:

-   `docx_to_markdown.py`
-   `markdown_to_docx.py`
-   `batch.py`

Responsibilities:

-   Deterministic conversion behavior
-   Output validation
-   Parallel batch execution
-   Version suffix integration

------------------------------------------------------------------------

### 3. Versioning Utility

    src/docutil/utils/versioning.py

Generates deterministic filename suffixes:

    document_2026-02-14_v1.md
    document_2026-02-14_v2.md

Guarantees:

-   No overwrites
-   Chronological ordering
-   Multi-run safety

------------------------------------------------------------------------

### 4. Doctor Diagnostics

    src/docutil/doctor.py

Performs environment validation:

-   Python version check
-   Pandoc availability
-   Write permissions
-   PATH resolution

Safe for CI pipelines.

------------------------------------------------------------------------

### 5. Logging System

    src/docutil/logging_utils.py

Supports:

-   INFO and DEBUG levels
-   Structured logs
-   Optional file output
-   CI-friendly formatting

------------------------------------------------------------------------

## Batch Engine Design

The batch engine supports:

-   Recursive discovery
-   TTY-aware progress bars
-   Dry-run safety mode
-   Parallel execution
-   Deterministic output mapping

Parallelism is implemented using `ThreadPoolExecutor`.

------------------------------------------------------------------------

## Dependency Strategy

Core runtime dependencies are intentionally minimal:

-   typer
-   pypandoc
-   tqdm

Optional extras:

-   python-docx (for metadata inspection)

------------------------------------------------------------------------

## Testing Strategy

Testing is divided into:

-   Unit tests (conversion logic)
-   CLI tests (Typer commands)
-   Versioning tests
-   Batch execution tests

All tests run in CI across:

-   Python 3.10
-   Python 3.11
-   Python 3.12

------------------------------------------------------------------------

## CI/CD Pipeline

GitHub Actions pipeline includes:

-   Ruff linting
-   Ruff formatting
-   MyPy static typing
-   Pytest execution
-   Environment doctor validation

------------------------------------------------------------------------

## Design Principles

docutil follows these engineering principles:

-   Deterministic output
-   No hidden side effects
-   Explicit flags over implicit behavior
-   Reproducible builds
-   CI-first design
-   Enterprise maintainability

------------------------------------------------------------------------

## Future Architecture Extensions

Planned enhancements:

-   Plugin-based converter registry
-   Configuration file support
-   Watch mode (filesystem monitor)
-   Structured JSON logging mode
-   Cloud storage adapters (S3, Azure Blob)

------------------------------------------------------------------------

docutil is designed not as a script, but as an extensible automation
platform.
