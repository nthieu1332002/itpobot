import json
import hashlib
from pathlib import Path

MANIFEST_PATH = Path(
    "storage/manifests/article_manifest.json"
)


def load_manifest():
    if not MANIFEST_PATH.exists():
        return {}

    content = MANIFEST_PATH.read_text(encoding="utf-8").strip()

    if not content:
        return {}

    return json.loads(content)


def save_manifest(data):
    MANIFEST_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        MANIFEST_PATH,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            data,
            f,
            indent=2,
        )


def build_article_hash(article):
    content = (
        article["title"]
        + article["updated_at"]
        + article["body"]
    )

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()
    
    
def detect_change(
    article,
    manifest,
):
    article_id = str(
        article["id"]
    )

    current_hash = build_article_hash(
        article
    )

    old_record = manifest.get(
        article_id
    )

    if not old_record:
        return "added"

    if (
        old_record["hash"]
        != current_hash
    ):
        return "updated"

    return "skipped"