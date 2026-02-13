from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DocxMetadata:
    path: str
    title: str | None
    author: str | None
    last_modified_by: str | None
    created: str | None
    modified: str | None


def inspect_docx_metadata(input_path: Path | str) -> DocxMetadata:
    """
    Extract core DOCX metadata.

    Requires python-docx:
      pip install ".[docx]"
    """
    input_path = Path(input_path).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != ".docx":
        raise ValueError("Input file must be a .docx document.")

    try:
        from docx import Document  # type: ignore
    except Exception as exc:
        raise RuntimeError(
            "python-docx is not installed. Install with: pip install '.[docx]'"
        ) from exc

    doc = Document(str(input_path))
    props = doc.core_properties

    meta = DocxMetadata(
        path=str(input_path),
        title=getattr(props, "title", None),
        author=getattr(props, "author", None),
        last_modified_by=getattr(props, "last_modified_by", None),
        created=str(getattr(props, "created", None)) if getattr(props, "created", None) else None,
        modified=str(getattr(props, "modified", None))
        if getattr(props, "modified", None)
        else None,
    )

    logger.info("DOCX metadata extracted: %s", asdict(meta))
    return meta
