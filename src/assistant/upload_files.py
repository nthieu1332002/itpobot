from pathlib import Path

from src.assistant.openai_client import client
from src.assistant.vector_store import (
    get_or_create_vector_store,
)

ARTICLES_DIR = Path(
    "storage/articles"
)


def upload_articles():
    vector_store_id = (
        get_or_create_vector_store()
    )

    files = []

    for md_file in ARTICLES_DIR.glob(
        "*.md"
    ):
        files.append(
            open(
                md_file,
                "rb",
            )
        )

    print(
        f"Uploading {len(files)} files..."
    )

    batch = (
        client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=files,
        )
    )

    print(
        f"Status: {batch.status}"
    )

    print(
        f"Completed: {batch.file_counts.completed}"
    )

    print(
        f"Failed: {batch.file_counts.failed}"
    )

    for f in files:
        f.close()


if __name__ == "__main__":
    upload_articles()