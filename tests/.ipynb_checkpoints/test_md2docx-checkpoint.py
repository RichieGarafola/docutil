from unittest.mock import patch


def test_md2docx_calls_pandoc(tmp_md):
    from docutil.conversions.markdown_to_docx import markdown_to_docx

    with patch("pypandoc.convert_file") as mock:
        markdown_to_docx(tmp_md)
        mock.assert_called_once()
