from __future__ import annotations

"""
Environment Diagnostics (doctor)
===============================

Provides environment validation to quickly diagnose
common setup issues.

Design Goals
------------
• zero side effects
• fast
• CI safe
• human readable
• actionable errors

Usage
------
docutil doctor
"""

import platform
import shutil
import sys
from pathlib import Path

import typer

from docutil.pandoc_utils import get_pandoc_status

app = typer.Typer(add_completion=False)


def _check_write_permissions() -> bool:
    try:
        test = Path(".docutil_write_test.tmp")
        test.write_text("ok")
        test.unlink()
        return True
    except Exception:
        return False


@app.command()
def doctor() -> None:
    """Run environment diagnostics."""

    typer.echo("docutil environment check\n")

    # ---------------------------------------------------------
    # Python
    # ---------------------------------------------------------
    typer.echo(f"Python: {platform.python_version()}  ✓")

    # ---------------------------------------------------------
    # Pandoc
    # ---------------------------------------------------------
    status = get_pandoc_status()
    if status.available:
        typer.echo(f"Pandoc: {status.version or 'found'}  ✓")
    else:
        typer.echo("Pandoc: NOT FOUND  ✗")
        typer.echo("  Install: conda install -c conda-forge pandoc")

    # ---------------------------------------------------------
    # Write permissions
    # ---------------------------------------------------------
    if _check_write_permissions():
        typer.echo("Write permissions: ✓")
    else:
        typer.echo("Write permissions: ✗")

    # ---------------------------------------------------------
    # PATH
    # ---------------------------------------------------------
    typer.echo(f"pandoc path: {shutil.which('pandoc')}")
