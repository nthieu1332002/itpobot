from src.scraper.exporter import (
    build_filename,
    build_markdown_document,
    yaml_safe_string,
    sanitize_markdown,
)


def test_build_filename_creates_slug():
    filename = build_filename("How to Add YouTube Video", 12345)
    assert filename == "how-to-add-youtube-video_12345.md"


def test_build_filename_handles_special_characters():
    filename = build_filename("What's New? (2024 Update!)", 99)
    assert "99.md" in filename
    assert "/" not in filename
    assert "?" not in filename


def test_build_filename_handles_empty_title():
    filename = build_filename("", 1)
    assert filename == "article_1.md"


def test_yaml_safe_string_escapes_quotes():
    result = yaml_safe_string('He said "hello"')
    assert '"' in result


def test_yaml_safe_string_handles_none():
    result = yaml_safe_string(None)
    assert result == '""'


def test_sanitize_markdown_removes_null_bytes():
    text = "Hello\x00World"
    result = sanitize_markdown(text)
    assert "\x00" not in result
    assert "HelloWorld" in result


def test_build_markdown_document_includes_frontmatter():
    article = {
        "title": "Test Article",
        "id": 123,
        "html_url": "https://support.optisigns.com/article/123",
        "updated_at": "2024-01-01T00:00:00Z",
    }
    result = build_markdown_document(article, "# Content\n\nBody here")
    assert "---" in result
    assert "Test Article" in result
    assert "123" in result
    assert "# Content" in result
    assert "Body here" in result
    assert "Source:" in result
