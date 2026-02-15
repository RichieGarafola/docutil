# src/docutil/pandoc_utils.py

from __future__ import annotations

import logging
import os
import shutil
from dataclasses import dataclass

import pypandoc
from packaging.version import Version

logger = logging.getLogger(__name__)
MIN_PANDOC_VERSION = Version("3.0")

from docutil.errors import PandocNotFoundError


@dataclass(frozen=True)
class PandocStatus:
    """
    Represents Pandoc availability and version.

    Attributes
    ----------
    available : bool
        Whether pandoc is available.
    path : str | None
        Path to pandoc binary if found.
    version : str | None
        Version string if available.
    """

    available: bool
    path: str | None
    version: str | None


def get_pandoc_status() -> PandocStatus:
    """
    Determine whether pandoc is available and return its status.
    """
    pandoc_path = shutil.which("pandoc")
    if not pandoc_path:
        return PandocStatus(available=False, path=None, version=None)

    try:
        ver = pypandoc.get_pandoc_version()
        return PandocStatus(available=True, path=pandoc_path, version=str(ver))
    except Exception:
        return PandocStatus(available=True, path=pandoc_path, version=None)


def require_pandoc() -> None:
    """
    Ensures Pandoc is installed and accessible.

    Can be skipped in test environments via:
        DOCUTIL_SKIP_PANDOC_CHECK=1
    """

    if os.getenv("DOCUTIL_SKIP_PANDOC_CHECK") == "1":
        return

    if not shutil.which("pandoc"):
        raise PandocNotFoundError(
            "Pandoc executable not found on PATH. Install via: conda install -c conda-forge pandoc"
        )

    try:
        pypandoc.get_pandoc_version()
    except OSError as exc:
        raise PandocNotFoundError("Pandoc installation detected but not functioning.") from exc
