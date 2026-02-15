from __future__ import annotations

"""
docutil CLI
===========

Command-line interface for the docutil toolkit.

Design Goals
------------
• Deterministic behavior
• Explicit flags (no hidden side effects)
• Safe defaults (no overwrites unless forced)
• Scriptable for CI/CD
• Human-readable output
• Machine-readable (JSON) where appropriate
• Zero external system dependencies
"""

import json
import logging
from collections.abc import Callable
from pathlib import Path
from typing import Literal

import typer

from docutil import __version__
from docutil.conversions.batch import batch_convert
from docutil.conversions.docx_to_markdown import docx_to_markdown
from docutil.conversions.markdown_to_docx import markdown_to_docx
from docutil.doctor import run_doctor
from docutil.inspect.docx_metadata import inspect_docx_metadata
from docutil.logging_utils import configure_logging
from docutil.templates import scaffold_project
from docutil.utils.version_bump import bump_version
from docutil.utils.versioning import generate_versioned_path

# -----------------------------------------------------------------------------
# Typer App Setup
# -----------------------------------------------------------------------------

app = typer.Typer(
    add_completion=False,
    help="""
docutil — Enterprise Document Utility Toolkit

Convert, inspect, and scaffold document workflows powered by Pandoc.

Common Commands:
  docutil doctor
  docutil version
  docutil docx2md input.docx
  docutil batch docx2md ./docs --recursive
  docutil inspect docx file.docx
""",
)

inspect_app = typer.Typer(add_completion=False)

app.add_typer(inspect_app, name="inspect")

logger = logging.getLogger(__name__)


@app.command()
def doctor() -> None:
    """
    Validate local environment configuration.

    Checks:
      • Python version
      • Pandoc availability
      • Write permissions
      • PATH resolution

    Safe to run in CI environments.
    """
    run_doctor()


# -----------------------------------------------------------------------------
# Global Options
# -----------------------------------------------------------------------------


@app.callback()
def _main(
    verbose: bool = typer.Option(
        False,
        "--verbose",
        help="Enable debug logging.",
    ),
    log_file: Path | None = typer.Option(
        None,
        "--log-file",
        help="Optional log file path.",
    ),
) -> None:
    """Global CLI options."""
    configure_logging(level=logging.DEBUG if verbose else logging.INFO, log_file=log_file)


# -----------------------------------------------------------------------------
# Version
# -----------------------------------------------------------------------------


@app.command()
def version() -> None:
    """Print installed docutil version."""
    typer.echo(__version__)


# -----------------------------------------------------------------------------
# Single File Conversions
# -----------------------------------------------------------------------------


@app.command("docx2md")
def cli_docx2md(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        help="Path to the input DOCX file.",
    ),
    output_path: Path | None = typer.Argument(
        None,
        help="Optional output path. Defaults to input filename with .md extension.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite existing output.",
    ),
    versioned: bool = typer.Option(
        False,
        "--versioned",
        help="Append date + per-day version suffix (e.g., _2026-02-14_v1).",
    ),
) -> None:
    """
    Convert DOCX → Markdown.

    Examples:
      docutil docx2md input.docx
      docutil docx2md input.docx output.md --versioned
    """

    if output_path is None:
        output_path = input_path.with_suffix(".md")

    if versioned:
        output_path = generate_versioned_path(output_path)

    if output_path.exists() and not (force or versioned):
        typer.echo("Output exists. Use --force or --versioned.")
        raise typer.Exit(code=1)

    typer.echo(docx_to_markdown(input_path, output_path))


@app.command("md2docx")
def cli_md2docx(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        help="Path to the input Markdown file.",
    ),
    output_path: Path | None = typer.Argument(
        None,
        help="Optional output path. Defaults to input filename with .docx extension.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite existing output.",
    ),
    versioned: bool = typer.Option(
        False,
        "--versioned",
        help="Append date + per-day version suffix (e.g., _2026-02-14_v1).",
    ),
) -> None:
    """
    Convert Markdown → DOCX.

    Examples:
      docutil md2docx input.md
      docutil md2docx input.md output.docx --versioned
    """

    if output_path is None:
        output_path = input_path.with_suffix(".docx")

    if versioned:
        output_path = generate_versioned_path(output_path)

    if output_path.exists() and not force:
        typer.echo("Output exists. Use --force or --versioned.")
        raise typer.Exit(code=1)

    typer.echo(markdown_to_docx(input_path, output_path))


# -----------------------------------------------------------------------------
# Batch Conversion
# -----------------------------------------------------------------------------


@app.command("batch")
def cli_batch(
    mode: Literal["docx2md", "md2docx"] = typer.Argument(
        ...,
        help="Conversion mode.",
    ),
    folder: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=False,
        dir_okay=True,
        help="Folder containing files to convert.",
    ),
    recursive: bool = typer.Option(False, "--recursive", help="Search folders recursively."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview work without writing files."),
    force: bool = typer.Option(False, "--force", help="Overwrite existing outputs."),
    versioned: bool = typer.Option(
        False,
        "--versioned",
        help="Append date + per-day version suffix to each output file.",
    ),
    out_folder: Path | None = typer.Option(None, "--out-folder", help="Optional output folder."),
    no_progress: bool = typer.Option(False, "--no-progress", help="Disable progress bar."),
    workers: int = typer.Option(1, "--workers", min=1, help="Number of parallel workers."),
) -> None:
    """Batch convert files inside a folder.

    Examples:
      docutil batch docx2md ./docs
      docutil batch docx2md ./docs --recursive
      docutil batch docx2md ./docs --out-folder ./converted
      docutil batch docx2md ./docs --versioned
    """
    modes: dict[str, tuple[str, str, Callable[[Path, Path | None], Path]]] = {
        "docx2md": (".docx", ".md", docx_to_markdown),
        "md2docx": (".md", ".docx", markdown_to_docx),
    }

    input_suffix, output_suffix, converter = modes[mode]

    batch_convert(
        folder,
        input_suffix,
        converter,
        output_folder=out_folder,
        output_suffix=output_suffix if out_folder else None,
        recursive=recursive,
        dry_run=dry_run,
        force=force,
        versioned=versioned,
        progress=not no_progress,
        workers=workers,
    )


@inspect_app.command("docx")
def cli_inspect_docx(
    path: Path = typer.Argument(..., exists=True, help="DOCX file to inspect."),
    json_flag: bool = typer.Option(False, "--json", help="Output JSON."),
) -> None:
    """Inspect DOCX metadata (requires optional extra `docx`)."""
    meta = inspect_docx_metadata(path)
    if json_flag:
        typer.echo(json.dumps(meta.__dict__, indent=2))
    else:
        typer.echo(meta)


@app.command("scaffold")
def cli_scaffold(
    kind: str = typer.Argument(
        ...,
        help="Template type. Currently only 'project' is supported.",
    ),
    name: str = typer.Argument(..., help="Project name."),
    out_dir: Path = typer.Argument(..., help="Output directory."),
    force: bool = typer.Option(False, "--force", help="Overwrite existing output directory."),  # noqa: FBT003
) -> None:
    """Generate a project template skeleton.

    Example:
      docutil scaffold project MyProject ./output
    """
    if kind != "project":
        raise typer.BadParameter("Only 'project' supported.")

    typer.echo(scaffold_project(name, out_dir, force=force))


# -----------------------------------------------------------------------------
# Bump-version
# -----------------------------------------------------------------------------
@app.command("bump-version")
def cli_bump_version(
    part: Literal["major", "minor", "patch"] = typer.Argument("patch"),
) -> None:
    """
    Bump semantic version in pyproject.toml.
    """

    new_version = bump_version(Path("pyproject.toml"), part)
    typer.echo(f"Version bumped to {new_version}")
