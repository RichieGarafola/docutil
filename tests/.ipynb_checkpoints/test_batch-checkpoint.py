from docutil.conversions.batch import batch_convert


def test_dry_run(tmp_path):
    f = tmp_path / "a.md"
    f.write_text("hi")

    called = False

    def conv(src, out):
        nonlocal called
        called = True
        return src

    batch_convert(tmp_path, ".md", conv, dry_run=True)

    assert not called
