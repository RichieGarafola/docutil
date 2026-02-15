from datetime import date
from pathlib import Path

from docutil.utils.versioning import generate_versioned_path


def test_generate_versioned_path_creates_v1(tmp_path: Path, monkeypatch):
    """
    First call should create _v1 suffix.
    """

    test_file = tmp_path / "report.md"

    # Freeze date
    monkeypatch.setattr(
        "docutil.utils.versioning.date",
        type("MockDate", (), {"today": staticmethod(lambda: date(2026, 2, 14))}),
    )

    versioned = generate_versioned_path(test_file)

    assert versioned.name == "report_2026-02-14_v1.md"


def test_generate_versioned_path_increments_version(tmp_path: Path, monkeypatch):
    """
    If v1 exists, next call should return v2.
    """

    monkeypatch.setattr(
        "docutil.utils.versioning.date",
        type("MockDate", (), {"today": staticmethod(lambda: date(2026, 2, 14))}),
    )

    v1 = tmp_path / "report_2026-02-14_v1.md"
    v1.write_text("existing")

    base = tmp_path / "report.md"

    versioned = generate_versioned_path(base)

    assert versioned.name == "report_2026-02-14_v2.md"


def test_multiple_existing_versions(tmp_path: Path, monkeypatch):
    """
    Should skip to next available version.
    """

    monkeypatch.setattr(
        "docutil.utils.versioning.date",
        type("MockDate", (), {"today": staticmethod(lambda: date(2026, 2, 14))}),
    )

    for i in range(1, 4):
        (tmp_path / f"report_2026-02-14_v{i}.md").write_text("x")

    base = tmp_path / "report.md"
    versioned = generate_versioned_path(base)

    assert versioned.name == "report_2026-02-14_v4.md"
