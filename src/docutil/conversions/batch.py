from __future__ import annotations

"""
Batch Conversion Engine
======================

Centralized conversion runner used by CLI and tests.

Features
--------
• dry-run support
• force overwrite control
• progress bars (TTY aware)
• parallel workers
• out-folder structure preservation
• deterministic behavior
"""

import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Callable, Iterable, Optional

from tqdm import tqdm

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# File discovery
# -----------------------------------------------------------------------------


def iter_files(folder: Path, suffix: str, recursive: bool) -> Iterable[Path]:
    pattern = f"**/*{suffix}" if recursive else f"*{suffix}"
    yield from folder.glob(pattern)


# -----------------------------------------------------------------------------
# Core batch runner
# -----------------------------------------------------------------------------


def batch_convert(
    input_folder: Path | str,
    suffix: str,
    converter: Callable[[Path, Optional[Path]], Path],
    *,
    output_folder: Optional[Path | str] = None,
    recursive: bool = False,
    dry_run: bool = False,
    force: bool = False,
    progress: bool = True,
    workers: int = 1,
) -> list[Path]:
    """
    Batch convert files.

    Parameters
    ----------
    dry_run
        Only print planned conversions.
    force
        Overwrite existing outputs.
    progress
        Show tqdm progress if stdout is TTY.
    workers
        Parallel worker count.
    """

    input_folder = Path(input_folder).resolve()

    if not input_folder.exists():
        raise FileNotFoundError(input_folder)

    files = list(iter_files(input_folder, suffix, recursive))

    logger.info(
        "Batch start | folder=%s | files=%s | recursive=%s | dry_run=%s | workers=%s",
        input_folder,
        len(files),
        recursive,
        dry_run,
        workers,
    )

    if not files:
        return []

    if output_folder:
        output_folder = Path(output_folder).resolve()

    use_progress = progress and sys.stdout.isatty() and not dry_run

    results: list[Path] = []

    def build_output_path(src: Path) -> Optional[Path]:
        if not output_folder:
            return None

        relative = src.relative_to(input_folder)
        out = (output_folder / relative).with_suffix("")
        out.parent.mkdir(parents=True, exist_ok=True)
        return out

    def task(src: Path) -> Path:
        out = build_output_path(src)

        if out and out.exists() and not force:
            logger.debug("Skipping existing: %s", out)
            return out

        if dry_run:
            logger.info("DRY RUN: %s", src)
            return src

        return converter(src, out)

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

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
