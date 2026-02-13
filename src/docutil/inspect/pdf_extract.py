from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PdfExtractResult:
    path: str
    pages: int
    text: str


def extract_pdf_text(input_path: Path | str) -> PdfExtractResult:
    """
    Extract text from a PDF (best-effort).

    Requires PyMuPDF:
      pip install ".[pdf]"
    """
    input_path = Path(input_path).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != ".pdf":
        raise ValueError("Input file must be a .pdf document.")

    try:
        import fitz
    except Exception as exc:
        raise RuntimeError("PyMuPDF not installed. Install with: pip install '.[pdf]'") from exc

    doc = fitz.open(str(input_path))
    pages = doc.page_count

    chunks: list[str] = []
    for i in range(pages):
        page = doc.load_page(i)
        chunks.append(page.get_text("text"))

    text = "\n".join(chunks).strip()
    logger.info("PDF extracted: %s pages", pages)

    return PdfExtractResult(path=str(input_path), pages=pages, text=text)
