from src.assistant.openai_client import client
from src.assistant.vector_store import (
    get_or_create_vector_store,
)


def upload_files(
    file_paths: list[str],
):
    if not file_paths:
        print(
            "No files to upload."
        )
        return None

    vector_store_id = (
        get_or_create_vector_store()
    )

    files = []

    try:
        for path in file_paths:
            files.append(
                open(
                    path,
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

        return batch

    finally:
        for f in files:
            f.close()