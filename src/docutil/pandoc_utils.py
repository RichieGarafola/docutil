# src/docutil/pandoc_utils.py

from __future__ import annotations

import logging
import shutil
from dataclasses import dataclass

import pypandoc
from packaging.version import Version

logger = logging.getLogger(__name__)
MIN_PANDOC_VERSION = Version("3.0")


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
    Ensure Pandoc exists and meets minimum version.

    Deterministic conversion requires stable Pandoc behavior.
    """
    path = shutil.which("pandoc")

    if not path:
        raise RuntimeError("Pandoc not found. Install via:\nconda install -c conda-forge pandoc")

    version = Version(str(pypandoc.get_pandoc_version()))

    if version < MIN_PANDOC_VERSION:
        raise RuntimeError(f"Pandoc >= {MIN_PANDOC_VERSION} required (found {version})")

    logger.debug("Pandoc OK: %s (%s)", path, version)
