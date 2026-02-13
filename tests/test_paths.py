from pathlib import Path


def test_project_paths_smoke() -> None:
    # This test is intentionally minimal — it's here to validate the test harness.
    assert isinstance(Path.cwd(), Path)
