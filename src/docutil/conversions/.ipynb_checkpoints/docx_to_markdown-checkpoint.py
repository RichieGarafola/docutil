from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import pypandoc
from docutil.pandoc_utils import require_pandoc

logger = logging.getLogger(__name__)


def docx_to_markdown(input_path: Path | str, output_path: Optional[Path | str] = None) -> Path:
    """
    Convert a .docx file to GitHub-Flavored Markdown (GFM).

    Deterministic output:
        • ATX headings
        • no line wrapping

    Returns
    -------
    Path
        Path to generated Markdown file
    """
    require_pandoc()

    input_path = Path(input_path).expanduser()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != ".docx":
        raise ValueError("Input file must be a .docx document.")

    output_path = Path(output_path).resolve() if output_path else input_path.with_suffix(".md")

    logger.info("DOCX → Markdown | %s → %s", input_path.name, output_path.name)

    pypandoc.convert_file(
        str(input_path),
        to="gfm",
        format="docx",
        outputfile=str(output_path),
        extra_args=["--wrap=none", "--markdown-headings=atx"],
    )

    return output_path
