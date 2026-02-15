# Versioning System

## Overview

docutil implements **detinistic, collision-safe, per-day versioned file
naming**.

This system ensures:

-   No accidental overwrites
-   Clean audit trails
-   Deterministic naming
-   CI/CD friendly outputs
-   Enterprise-safe document history

------------------------------------------------------------------------

## How Versioning Works

When the `--versioned` flag is enabled, docutil appends:

    _YYYY-MM-DD_vN

Where:

-   `YYYY-MM-DD` = current system date
-   `vN` = incremental version number for that day
-   `N` starts at 1 and increments automatically

------------------------------------------------------------------------

## Example

Original file:

    report.md

First conversion (same day):

    report_2026-02-14_v1.md

Second conversion:

    report_2026-02-14_v2.md

Third conversion:

    report_2026-02-14_v3.md

------------------------------------------------------------------------

## CLI Usage

### Single File Conversion

``` bash
docutil docx2md report.docx --versioned
docutil md2docx report.md --versioned
```

### Batch Mode

``` bash
docutil batch docx2md ./docs --versioned
```

------------------------------------------------------------------------

## Conflict Handling Logic

If `--versioned` is used:

-   Existing files are NEVER overwritten
-   Version increments automatically
-   No `--force` required

If `--versioned` is NOT used:

-   Existing files require `--force`
-   Otherwise command exits safely

------------------------------------------------------------------------

## Internal Implementation

Versioning is handled by:

    docutil.utils.versioning.generate_versioned_path()

The function:

1.  Extracts base filename
2.  Determines current date
3.  Scans directory for existing versions
4.  Increments version counter
5.  Returns collision-free path

------------------------------------------------------------------------

## Determinism & Safety

The system guarantees:

-   Stable naming pattern
-   No randomness
-   No UUIDs
-   No timestamps with seconds
-   Clean reproducible builds

This makes it safe for:

-   CI pipelines
-   Regulated environments
-   Document compliance workflows
-   Government contracting environments

------------------------------------------------------------------------

## Best Practices

Recommended usage:

-   Always use `--versioned` in production
-   Use non-versioned mode only in controlled environments
-   Pair with semantic version bumps for release control

------------------------------------------------------------------------

## Related Commands

    docutil bump-version patch
    docutil bump-version minor
    docutil bump-version major

Versioned outputs + semantic project versioning provide full lifecycle
traceability.

------------------------------------------------------------------------

## Summary

docutil versioning provides:

-   Enterprise-grade safety
-   Deterministic naming
-   Clean audit trails
-   Zero overwrite risk
-   CI/CD compatibility

It is designed for professional document automation workflows.
