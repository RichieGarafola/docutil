from __future__ import annotations

"""Batch Conversion Engine

Centralized conversion runner used by CLI and tests.

Features
--------
- dry-run support
- force overwrite control
- progress bars (TTY aware)
- parallel workers
- out-folder structure preservation
- deterministic behavior
- optional date+version suffixing (per output file)
"""

import logging
import sys
from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from tqdm import tqdm

from docutil.utils.versioning import generate_versioned_path

logger = logging.getLogger(__name__)


def iter_files(folder: Path, suffix: str, recursive: bool) -> Iterable[Path]:
    """Yield files in *folder* matching *suffix*."""
    pattern = f"**/*{suffix}" if recursive else f"*{suffix}"
    yield from folder.glob(pattern)


def batch_convert(
    input_folder: Path | str,
    input_suffix: str,
    converter: Callable[[Path, Path | None], Path],
    *,
    output_folder: Path | str | None = None,
    output_suffix: str | None = None,
    recursive: bool = False,
    dry_run: bool = False,
    force: bool = False,
    versioned: bool = False,
    progress: bool = True,
    workers: int = 1,
) -> list[Path]:
    """Batch convert files.

    Parameters
    ----------
    input_folder
        Folder to scan for inputs.
    input_suffix
        Input file suffix to match (e.g., ".docx").
    converter
        Callable that accepts (src_path, out_path_or_none) and returns output Path.
    output_folder
        If provided, outputs are written under this folder preserving relative structure.
    output_suffix
        If provided, forces the output extension (e.g., ".md"). Required when using
        *output_folder* so outputs get correct file extensions.
    recursive
        Whether to search subfolders.
    dry_run
        Only log planned conversions; do not write files.
    force
        Overwrite existing outputs (if False and file exists, that file is skipped unless
        versioned=True).
    versioned
        If True, append `_YYYY-MM-DD_vN` to each output filename.
    progress
        Show tqdm progress if stdout is a TTY and not dry-run.
    workers
        Parallel worker count.
    """

    input_folder = Path(input_folder).resolve()

    if not input_folder.exists():
        raise FileNotFoundError(input_folder)

    if output_folder and not output_suffix:
        raise ValueError("output_suffix is required when output_folder is provided.")

    files = list(iter_files(input_folder, input_suffix, recursive))

    logger.info(
        (
            "Batch start | folder=%s | files=%s | "
            "recursive=%s | dry_run=%s | "
            "workers=%s | versioned=%s"
        ),
        input_folder,
        len(files),
        recursive,
        dry_run,
        workers,
        versioned,
    )

    if not files:
        return []

    out_root = Path(output_folder).resolve() if output_folder else None
    use_progress = progress and sys.stdout.isatty() and not dry_run

    results: list[Path] = []

    def build_output_path(src: Path) -> Path | None:
        if out_root is None:
            return None

        rel = src.relative_to(input_folder)
        out = (out_root / rel).with_suffix(output_suffix or "")

        out.parent.mkdir(parents=True, exist_ok=True)

        if versioned:
            out = generate_versioned_path(out)

        return out

    def task(src: Path) -> Path:
        out = build_output_path(src)

        if out and out.exists() and not (force or versioned):
            logger.debug("Skipping existing: %s", out)
            return out

        if dry_run:
            logger.info("DRY RUN: %s", src)
            return src

        return converter(src, out)

    if workers <= 1:
        iterable = tqdm(files, disable=not use_progress)
        for f in iterable:
            results.append(task(f))
    else:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futures = [ex.submit(task, f) for f in files]
            iterable = tqdm(as_completed(futures), total=len(futures), disable=not use_progress)
            for fut in iterable:
                results.append(fut.result())

    logger.info("Batch complete | outputs=%s", len(results))
    return results
