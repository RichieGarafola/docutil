"""
Templates / Scaffolding Utilities
=================================

Provides project scaffolding helpers for documentation-heavy or
automation-focused repositories.

Design Goals
------------
• Deterministic folder structure
• Idempotent (safe to run multiple times)
• No accidental overwrites
• Professional defaults
• Enterprise / CI friendly

Typical Usage
-------------
>>> scaffold_project("MyTool", "./workspace")

Creates:

MyTool/
├── README.md
├── docs/
├── src/
├── tests/
└── .gitignore
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

logger = logging.getLogger(__name__)

__all__ = ["scaffold_project"]


# -----------------------------------------------------------------------------
# Internal helpers
# -----------------------------------------------------------------------------

def _safe_write(path: Path, content: str, *, force: bool = False) -> None:
    """
    Write text file safely.

    Default behavior:
        • Do NOT overwrite existing files (idempotent)

    If force=True:
        • Overwrite existing files
    """
    if force or not path.exists():
        path.write_text(content, encoding="utf-8")


def _create_dirs(dirs: Iterable[Path]) -> None:
    """Create directories if missing (safe + idempotent)."""
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------

def scaffold_project(
    project_name: str,
    output_dir: Path | str,
    *,
    force: bool = False,
) -> Path:
    """
    Create a clean project skeleton for documentation-heavy work.

    Parameters
    ----------
    project_name : str
        Name of the project folder.
    output_dir : Path | str
        Parent directory where project is created.
    force : bool, default False
        Overwrite README / .gitignore if they already exist.

    Returns
    -------
    Path
        Root project directory path.

    Notes
    -----
    Backwards compatibility:
        • With default arguments, behavior matches original implementation exactly.
        • Existing files are NOT overwritten.
    """

    if not project_name.strip():
        raise ValueError("project_name cannot be empty")

    output_dir = Path(output_dir).resolve()
    root = output_dir / project_name

    logger.info("Creating project scaffold: %s", root)

    # ------------------------------------------------------------------
    # Directory structure (same as original)
    # ------------------------------------------------------------------

    _create_dirs(
        [
            root,
            root / "docs",
            root / "src",
            root / "tests",
        ]
    )

    # ------------------------------------------------------------------
    # README (enhanced but backward compatible)
    # ------------------------------------------------------------------

    readme_content = (
        f"# {project_name}\n\n"
        "## Overview\n\n"
        "Describe the purpose of this project.\n\n"
        "## Quick Start\n\n"
        "## Development\n\n"
        "## Notes\n"
    )

    _safe_write(root / "README.md", readme_content, force=force)

    # ------------------------------------------------------------------
    # Gitignore (expanded but safe)
    # ------------------------------------------------------------------

    gitignore_content = (
        ".venv/\n"
        "__pycache__/\n"
        "*.pyc\n"
        ".DS_Store\n"
        ".idea/\n"
        ".vscode/\n"
        "build/\n"
        "dist/\n"
        "*.log\n"
    )

    _safe_write(root / ".gitignore", gitignore_content, force=force)

    logger.info("Project scaffold created successfully")

    return root
