"""
Conversions Package
===================

Provides deterministic, production-safe document format conversions.

All converters:
    • Validate inputs
    • Enforce Pandoc availability
    • Provide structured logging
    • Return explicit output paths
"""

from __future__ import annotations

from .docx_to_markdown import docx_to_markdown
from .markdown_to_docx import markdown_to_docx
from .batch import batch_convert

__all__ = [
    "docx_to_markdown",
    "markdown_to_docx",
    "batch_convert",
]
