import re
from markdownify import markdownify as md

def clean_html(html: str) -> str:
    html = re.sub(
        r'id="[^"]*"',
        "",
        html,
    )

    html = re.sub(
        r'data-[^=]+="[^"]*"',
        "",
        html,
    )

    return html

def html_to_markdown(html: str) -> str:
    cleaned_html = clean_html(html)
    return md(
        cleaned_html,
        heading_style="ATX",
    )