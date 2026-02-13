"""
Module entry point.

Allows:
    python -m docutil

This delegates execution to the Typer CLI while preserving
importability of the package without side effects.
"""

from __future__ import annotations

from docutil.cli import app

app()
