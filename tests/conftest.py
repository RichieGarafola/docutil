from pathlib import Path

import pytest


@pytest.fixture
def tmp_md(tmp_path: Path):
    p = tmp_path / "test.md"
    p.write_text("# Hello\n", encoding="utf-8")
    return p
