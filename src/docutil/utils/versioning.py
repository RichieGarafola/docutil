from __future__ import annotations

"""docutil.utils.versioning

Deterministic, human-friendly output versioning.

Naming convention
-----------------
Given an output path like:

    report.md

`generate_versioned_path(report.md)` produces:

    report_YYYY-MM-DD_v1.md

If called again on the same day (and v1 exists), it will produce v2, v3, ...

Design goals
------------
- No external dependencies
- Predictable, stable naming
- Works cross-platform
- Testable (date injection)

Notes
-----
This helper *does not* create the file. It only chooses a non-conflicting path.
"""

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

_VERSION_RE = re.compile(r"^(?P<stem>.+)_(?P<day>\d{4}-\d{2}-\d{2})_v(?P<ver>\d+)$")


@dataclass(frozen=True, slots=True)
class VersionedName:
    """Parsed representation of a versioned filename stem."""

    stem: str
    day: str
    version: int


def _today(override: date | None) -> date:
    return override if override is not None else date.today()


def _parse_versioned_stem(stem: str) -> VersionedName | None:
    match = _VERSION_RE.match(stem)
    if not match:
        return None
    return VersionedName(
        stem=match.group("stem"),
        day=match.group("day"),
        version=int(match.group("ver")),
    )


def generate_versioned_path(base_output: Path | str, *, today_override: date | None = None) -> Path:
    """Return a new path with a date + per-day incrementing version suffix.

    Parameters
    ----------
    base_output
        Target output path (must include suffix, e.g., .md, .docx).
    today_override
        For testing. If provided, uses this date instead of `date.today()`.

    Returns
    -------
    Path
        A path that does not currently exist, with a `_YYYY-MM-DD_vN` suffix.
    """
    base = Path(base_output)

    if base.suffix == "":
        raise ValueError("base_output must include a file extension (suffix).")

    day = _today(today_override).isoformat()

    # If the caller already passed a versioned name, keep the *un-versioned* stem
    # so repeated calls keep incrementing rather than nesting.
    parsed = _parse_versioned_stem(base.stem)
    stem = parsed.stem if parsed else base.stem

    # Find max existing version for this stem/day.
    parent = base.parent if base.parent != Path("") else Path(".")
    pattern = f"{stem}_{day}_v*{base.suffix}"

    max_ver = 0
    for p in parent.glob(pattern):
        parsed_existing = _parse_versioned_stem(p.stem)
        if parsed_existing and parsed_existing.day == day and parsed_existing.stem == stem:
            max_ver = max(max_ver, parsed_existing.version)

    next_ver = max_ver + 1
    candidate = parent / f"{stem}_{day}_v{next_ver}{base.suffix}"

    # Very defensive: avoid rare collisions (e.g., parallel writers) by probing.
    while candidate.exists():
        next_ver += 1
        candidate = parent / f"{stem}_{day}_v{next_ver}{base.suffix}"

    return candidate
