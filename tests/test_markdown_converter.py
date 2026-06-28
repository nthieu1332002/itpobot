from src.scraper.markdown_converter import (
    clean_html,
    html_to_markdown,
)


def test_clean_html_removes_id_attributes():
    html = '<div id="main-content"><p>Hello</p></div>'
    result = clean_html(html)
    assert 'id="main-content"' not in result
    assert "<p>Hello</p>" in result


def test_clean_html_removes_data_attributes():
    html = '<span data-testid="label" data-track="click">Text</span>'
    result = clean_html(html)
    assert "data-testid" not in result
    assert "data-track" not in result
    assert "Text" in result


def test_html_to_markdown_converts_headings():
    html = "<h1>Title</h1><p>Body text</p>"
    result = html_to_markdown(html)
    assert "# Title" in result
    assert "Body text" in result


def test_html_to_markdown_converts_lists():
    html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
    result = html_to_markdown(html)
    assert "Item 1" in result
    assert "Item 2" in result


def test_html_to_markdown_preserves_links():
    html = '<p>Visit <a href="https://example.com">here</a></p>'
    result = html_to_markdown(html)
    assert "https://example.com" in result
    assert "here" in result


def test_html_to_markdown_preserves_code_blocks():
    html = "<pre><code>print('hello')</code></pre>"
    result = html_to_markdown(html)
    assert "print('hello')" in result
