"""
Custom exception hierarchy for docutil.
"""


class DocutilError(Exception):
    """Base exception for all docutil errors."""


class PandocNotFoundError(DocutilError):
    """Raised when Pandoc is not available."""


class InvalidInputError(DocutilError):
    """Raised when user input is invalid."""


class ConversionError(DocutilError):
    """Raised when a document conversion fails."""
