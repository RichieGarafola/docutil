from __future__ import annotations

"""
Logging Utilities
================

Provides consistent, idempotent logging configuration for both:

• CLI usage
• library imports
• test environments

Design Goals
------------
• No duplicate handlers
• Safe to call multiple times
• Optional file logging
• Human-readable format
"""

import logging
from pathlib import Path

DEFAULT_FMT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(
    *,
    level: int = logging.INFO,
    log_file: Path | str | None = None,
) -> logging.Logger:
    """
    Configure console + optional file logging.

    Safe to call repeatedly (idempotent).
    """

    root = logging.getLogger()

    # ------------------------------------------------------------------
    # Prevent duplicate handlers (important for CLI + tests)
    # ------------------------------------------------------------------

    if not root.handlers:
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter(DEFAULT_FMT))
        root.addHandler(console)

    root.setLevel(level)

    # ------------------------------------------------------------------
    # Optional file logging
    # ------------------------------------------------------------------

    if log_file:
        path = Path(log_file).resolve()

        file_handler = logging.FileHandler(path, encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(DEFAULT_FMT))
        root.addHandler(file_handler)

    return root
