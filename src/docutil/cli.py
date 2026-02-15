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
    verbose: bool = typer.Option(False, "--verbose"),
    log_file: Path | None = typer.Option(None, "--log-file"),
) -> None:
    configure_logging(
        level=logging.DEBUG if verbose else logging.INFO,
        log_file=log_file,
    )


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
        help="Optional output file path. Defaults to same name with converted extension.",
    ),
    force: bool = typer.Option(False, "--force", help="Overwrite existing output"),
) -> None:
    """
    Convert a DOCX file to Markdown.

    Examples:
      docutil docx2md input.docx
      docutil docx2md input.docx output.md
      docutil docx2md input.docx output.md --force
    """

    if output_path and output_path.exists() and not force:
        typer.echo("Output exists. Use --force to overwrite.")
        raise typer.Exit(code=1)

    typer.echo(docx_to_markdown(input_path, output_path))


@app.command("md2docx")
def cli_md2docx(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        help="Path to the input markdown file.",
    ),
    output_path: Path | None = typer.Argument(
        None,
        help="Optional output file path. Defaults to same name with converted extension.",
    ),
    force: bool = typer.Option(False, "--force", help="Overwrite existing output"),
) -> None:
    """
    Convert a Markdown file to DOCX.

    Examples:
      docutil md2docx input.md
      docutil md2docx input.md output.docx
      docutil md2docx input.md output.docx --force
    """

    if output_path and output_path.exists() and not force:
        typer.echo("Output exists. Use --force to overwrite.")
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
        help="Folder containing files to convert.",
    ),
    recursive: bool = typer.Option(False, "--recursive", help="Search folders recursively."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without writing files."),
    force: bool = typer.Option(False, "--force", help="Overwrite existing files."),
    out_folder: Path | None = typer.Option(
        None,
        "--out-folder",
        help="Optional output folder.",
    ),
    no_progress: bool = typer.Option(False, "--no-progress", help="Disable progress bar."),
    workers: int = typer.Option(1, "--workers", help="Number of parallel workers."),
) -> None:
    """
    Batch convert files inside a folder.

    Modes:
      docx2md  Convert all .docx files to Markdown
      md2docx  Convert all .md files to DOCX

    Examples:
      docutil batch docx2md ./docs
      docutil batch docx2md ./docs --recursive
      docutil batch docx2md ./docs --out-folder ./converted
    """

    modes = {
        "docx2md": (".docx", docx_to_markdown),
        "md2docx": (".md", markdown_to_docx),
    }

    if mode not in modes:
        raise typer.BadParameter("mode must be docx2md | md2docx")

    suffix, converter = modes[mode]

    batch_convert(
        folder,
        suffix,
        converter,
        output_folder=out_folder,
        recursive=recursive,
        dry_run=dry_run,
        force=force,
        progress=not no_progress,
        workers=workers,
    )


# -----------------------------------------------------------------------------
# Inspect Commands
# -----------------------------------------------------------------------------


@inspect_app.command("docx")
def cli_inspect_docx(
    path: Path = typer.Argument(..., exists=True),
    json_flag: bool = typer.Option(False, "--json", help="Output JSON"),
) -> None:
    """Inspect DOCX metadata."""

    meta = inspect_docx_metadata(path)

    if json_flag:
        typer.echo(json.dumps(meta.__dict__, indent=2))
    else:
        typer.echo(meta)


# -----------------------------------------------------------------------------
# Scaffolding
# -----------------------------------------------------------------------------


@app.command("scaffold")
def cli_scaffold(
    kind: str = typer.Argument(
        ...,
        help="Template type. Currently only 'project' is supported.",
    ),
    name: str = typer.Argument(...),
    out_dir: Path = typer.Argument(...),
    force: bool = typer.Option(False, "--force"),
) -> None:
    """
    Generate a project template skeleton.

    Currently supported:
      project

    Example:
      docutil scaffold project MyProject ./output
    """
    if kind != "project":
        raise typer.BadParameter("Only 'project' supported.")

    typer.echo(scaffold_project(name, out_dir, force=force))
