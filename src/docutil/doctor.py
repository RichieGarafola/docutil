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
from pathlib import Path

from docutil.pandoc_utils import get_pandoc_status


def _check_write_permissions() -> bool:
    try:
        test = Path(".docutil_write_test.tmp")
        test.write_text("ok")
        test.unlink()
        return True
    except Exception:
        return False


def run_doctor() -> None:
    """Run environment diagnostics."""

    print("docutil environment check\n")

    # Python
    print(f"Python: {platform.python_version()}  ✓")

    # Pandoc
    status = get_pandoc_status()
    if status.available:
        print(f"Pandoc: {status.version or 'found'}  ✓")
    else:
        print("Pandoc: NOT FOUND  ✗")
        print("  Install: conda install -c conda-forge pandoc")

    # Write permissions
    if _check_write_permissions():
        print("Write permissions: ✓")
    else:
        print("Write permissions: ✗")

    # PATH
    print(f"pandoc path: {shutil.which('pandoc')}")
