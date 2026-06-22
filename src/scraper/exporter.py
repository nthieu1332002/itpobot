from pathlib import Path
from slugify import slugify
import json


def yaml_safe_string(value: str) -> str:
    return json.dumps(
        value or "",
        ensure_ascii=False,
    )


def sanitize_markdown(markdown: str) -> str:
    return markdown.replace(
        "\x00",
        "",
    )


def build_markdown_document(
    article,
    markdown,
):
    markdown = sanitize_markdown(markdown)

    return f"""---
title: {yaml_safe_string(article.get("title", ""))}
article_id: {article.get("id", "")}
url: {yaml_safe_string(article.get("html_url", ""))}
updated_at: {yaml_safe_string(article.get("updated_at", ""))}
---

{markdown}

---

Source: {article.get("html_url", "")}
"""


def build_filename(
    title: str,
    article_id: int,
):
    slug = slugify(title)

    if not slug:
        slug = "article"

    return f"{slug}_{article_id}.md"


def save_markdown(
    path: str,
    content: str,
):
    Path(path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        path,
        "w",
        encoding="utf-8",
        newline="\n",
    ) as f:
        f.write(content)