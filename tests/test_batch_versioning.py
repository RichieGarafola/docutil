from datetime import date
from pathlib import Path


def test_batch_versioning(tmp_path: Path):
    """
    Test versioning in batch conversion.
    """

    input_folder = tmp_path / "input_folder"
    input_folder.mkdir()

    file1 = input_folder / "test.docx"
    file1.write_text("test content")

    output_folder = tmp_path / "output_folder"
    output_folder.mkdir()

    from docutil.conversions.batch import batch_convert

    # Simple converter that writes output file and returns Path
    def fake_converter(src: Path, out: Path | None) -> Path:
        assert out is not None
        out = out.with_suffix(".md")
        out.write_text(f"Converted: {src.name}")
        return out

    # Run first time (should create v1)
    batch_convert(
        input_folder=input_folder,
        input_suffix=".docx",
        converter=fake_converter,
        output_folder=output_folder,
        output_suffix=".md",
        versioned=True,
    )

    today = date.today().isoformat()

    versioned_file_v1 = output_folder / f"test_{today}_v1.md"
    assert versioned_file_v1.exists()

    # Run second time (should create v2)
    batch_convert(
        input_folder=input_folder,
        input_suffix=".docx",
        converter=fake_converter,
        output_folder=output_folder,
        output_suffix=".md",
        versioned=True,
    )

    versioned_file_v2 = output_folder / f"test_{today}_v2.md"
    assert versioned_file_v2.exists()
