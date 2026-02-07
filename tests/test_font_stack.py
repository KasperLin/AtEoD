from pathlib import Path


def test_furo_font_stack_is_songti_first_for_chinese_text() -> None:
    css = Path("source/_static/custom.css").read_text(encoding="utf-8")

    # Furo sidebars/toc use --font-stack, so this variable must exist.
    assert "--font-stack:" in css
    assert "--font-stack--headings: var(--font-stack);" in css

    # Ensure Chinese serif stack prioritizes Songti and does not prefer PingFang.
    assert '"Songti SC"' in css
    assert '"PingFang SC"' not in css
