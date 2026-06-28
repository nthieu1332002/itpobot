from src.scraper.manifest import (
    build_article_hash,
    detect_change,
)


def make_article(title="Test", updated_at="2024-01-01", body="<p>Hello</p>"):
    return {
        "id": 123,
        "title": title,
        "updated_at": updated_at,
        "body": body,
    }


def test_build_article_hash_deterministic():
    article = make_article()
    hash1 = build_article_hash(article)
    hash2 = build_article_hash(article)
    assert hash1 == hash2


def test_build_article_hash_changes_with_content():
    article1 = make_article(body="<p>Hello</p>")
    article2 = make_article(body="<p>World</p>")
    assert build_article_hash(article1) != build_article_hash(article2)


def test_build_article_hash_changes_with_title():
    article1 = make_article(title="Title A")
    article2 = make_article(title="Title B")
    assert build_article_hash(article1) != build_article_hash(article2)


def test_detect_change_added_when_not_in_manifest():
    article = make_article()
    manifest = {}
    assert detect_change(article, manifest) == "added"


def test_detect_change_skipped_when_hash_matches():
    article = make_article()
    manifest = {
        "123": {"hash": build_article_hash(article), "updated_at": "2024-01-01"}
    }
    assert detect_change(article, manifest) == "skipped"


def test_detect_change_updated_when_hash_differs():
    article = make_article()
    manifest = {
        "123": {"hash": "old-hash-value", "updated_at": "2024-01-01"}
    }
    assert detect_change(article, manifest) == "updated"
