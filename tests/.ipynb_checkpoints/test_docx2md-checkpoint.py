from pathlib import Path
from unittest.mock import patch

from docutil.conversions.docx_to_markdown import docx_to_markdown



def test_calls_pandoc(tmp_path: Path):
    f = tmp_path / "x.docx"
    f.write_text("dummy")

    with patch("pypandoc.convert_file") as mock:
        docx_to_markdown(f)
        mock.assert_called_once()
