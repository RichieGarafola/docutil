from __future__ import annotations

import logging
from pathlib import Path

import pypandoc

from docutil.pandoc_utils import require_pandoc

logger = logging.getLogger(__name__)


def markdown_to_docx(input_path: Path | str, output_path: Path | str | None = None) -> Path:
    """Convert Markdown → DOCX."""
    require_pandoc()

    input_path = Path(input_path).expanduser()

    if not input_path.exists():
        raise FileNotFoundError(input_path)

    if input_path.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError("Input must be Markdown")

    output_path = Path(output_path).resolve() if output_path else input_path.with_suffix(".docx")

    logger.info("Markdown → DOCX | %s → %s", input_path.name, output_path.name)

    pypandoc.convert_file(
        str(input_path),
        to="docx",
        format="gfm",
        outputfile=str(output_path),
        extra_args=["--wrap=none"],
    )

    return output_path
