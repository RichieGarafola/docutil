
# docutil Technical Design Document

## Document Purpose

This document describes the technical architecture, design decisions, and implementation details for **docutil**, an enterprise‑grade document automation CLI.

Audience:
• Engineers
• Maintainers
• Contributors
• DevOps / CI owners

This is not a user guide. For usage examples see USERGUIDE.md.

---

# 1. System Overview

docutil is a **CLI‑first document processing toolkit** that provides deterministic and scriptable conversions between:

• DOCX  
• Markdown (GitHub Flavored Markdown)

Primary goals:

• automation
• reproducibility
• CI/CD compatibility
• zero GUI dependencies
• minimal runtime requirements

docutil wraps Pandoc with safe defaults and exposes a consistent Python + CLI interface.

---

# 2. Design Principles

## Deterministic
Same input → same output.

• fixed pandoc flags
• no implicit formatting
• no environment side effects

## Scriptable
Every action is a command.

• no prompts
• no interactive flows
• CI friendly

## Safe by Default
• no overwrite without --force
• dry‑run support
• clear error messages

## Testable
• business logic isolated from CLI
• pandoc mocked in tests
• fast unit tests (<1s)

## Minimal Dependencies
• Python + Pandoc only
• no GUI frameworks
• no system installers

---

# 3. High Level Architecture

```
User
  │
  ▼
CLI (Typer)
  │
  ▼
Conversion Engine
  │
  ▼
Pandoc
```

The CLI acts as a thin interface layer.
All logic resides in internal modules.

---

# 4. Repository Structure

```
src/docutil/
│
├── cli.py
├── doctor.py
├── logging_utils.py
│
├── conversions/
│   ├── batch.py
│   ├── docx_to_markdown.py
│   ├── markdown_to_docx.py
│
├── inspect/
│   └── docx_metadata.py
│
├── templates/
│   └── __init__.py
│
└── tests/
```

---

# 5. Component Design

## 5.1 CLI Layer (Typer)

Responsibilities:
• argument parsing
• validation
• user messaging
• logging configuration

Non‑Responsibilities:
• conversion logic
• file processing

The CLI calls library functions only.

Rationale:
Separates UI from business logic → easier testing.

---

## 5.2 Conversion Modules

### docx_to_markdown
• validates input
• enforces suffix
• calls pandoc with deterministic flags

### markdown_to_docx
• same validation pattern
• uses Pandoc GFM format

### markdown_to_pdf (optional)
• disabled unless PDF engine available

Each converter:
• pure function style
• returns output path
• raises explicit exceptions

---

## 5.3 Batch Engine

File: conversions/batch.py

Central execution engine for folder operations.

Features:
• recursive discovery
• dry run
• progress bars (TTY aware)
• parallel workers
• out‑folder mapping
• overwrite control

Responsibilities:
• orchestration only
• calls converter functions

This keeps converters simple and reusable.

---

## 5.4 Logging

File: logging_utils.py

Characteristics:
• idempotent setup
• console + optional file output
• consistent format

Reason:
Avoid duplicate handlers in CLI/tests.

---

## 5.5 Doctor

File: doctor.py

Purpose:
• environment diagnostics
• validate pandoc presence
• confirm write permissions

Goal:
Reduce support time for setup issues.

---

# 6. Data Flow

Single file:

CLI → converter → pandoc → output file

Batch:

CLI → batch engine → workers → converter → pandoc → outputs

---

# 7. Concurrency Model

Implementation:
ThreadPoolExecutor

Rationale:
Pandoc runs as external process → I/O bound
Threads sufficient and simpler than multiprocessing.

Workers configurable via:
--workers N

Default: 1 (safe)

---

# 8. Error Handling Strategy

Principles:
• fail fast
• explicit messages
• no silent skips

Examples:
• FileNotFoundError
• ValueError (wrong suffix)
• RuntimeError (pandoc missing)

Batch collects errors and logs failures.

---

# 9. Testing Strategy

Framework: pytest

## Unit Tests
• mock pandoc
• validate arguments
• fast (<1s)

## CLI Tests
• Typer CliRunner
• smoke tests

## Integration (optional)
• real pandoc
• small fixtures

---

# 10. Performance Characteristics

Single file:
~ instant

Batch:
Bound by pandoc execution time

Improvements:
• parallel workers
• SSD disk

---

# 11. Security Considerations

• no network calls
• local file operations only
• no shell injection (paths passed safely)
• no elevated privileges

Low risk footprint.

---

# 12. Extensibility

New formats can be added by:

1. creating new converter
2. registering in CLI
3. adding tests

Example future additions:
• HTML
• PDF (if engines available)
• plain text extraction

---

# 13. Future Enhancements

Planned:
• richer batch summaries
• additional metadata inspection
• packaging for PyPI
• integration test job
• enhanced stats reporting

---

# 14. Conclusion

docutil follows a simple architecture:

• thin CLI
• pure converters
• centralized batch engine
• deterministic behavior

This design maximizes:

• reliability
• maintainability
• testability
• portability

It is intentionally minimal and optimized for automation environments.
