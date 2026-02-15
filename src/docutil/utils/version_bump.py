import re
from pathlib import Path


def bump_version(pyproject_path: Path, part: str = "patch") -> str:
    """
    Bump semantic version inside pyproject.toml.

    part: major | minor | patch
    """

    text = pyproject_path.read_text()

    match = re.search(r'version\s*=\s*"(\d+)\.(\d+)\.(\d+)"', text)
    if not match:
        raise ValueError("Version not found in pyproject.toml")

    major, minor, patch = map(int, match.groups())

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    else:
        patch += 1

    new_version = f"{major}.{minor}.{patch}"

    updated_text = re.sub(
        r'version\s*=\s*"\d+\.\d+\.\d+"',
        f'version = "{new_version}"',
        text,
    )

    pyproject_path.write_text(updated_text)

    return new_version
