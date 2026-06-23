import json
from pathlib import Path

from src.assistant.openai_client import client

VECTOR_STORE_FILE = (
    Path("storage/vector_store.json")
)


def save_vector_store_id(
    vector_store_id: str,
):
    VECTOR_STORE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        VECTOR_STORE_FILE,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            {
                "vector_store_id": vector_store_id
            },
            f,
            indent=2,
        )


def load_vector_store_id():
    if not VECTOR_STORE_FILE.exists():
        return None

    with open(
        VECTOR_STORE_FILE,
        "r",
        encoding="utf-8",
    ) as f:
        data = json.load(f)

    return data.get(
        "vector_store_id"
    )


def get_or_create_vector_store():
    vector_store_id = (
        load_vector_store_id()
    )

    if vector_store_id:
        print(
            f"Using existing vector store: {vector_store_id}"
        )

        return vector_store_id

    vector_store = (
        client.vector_stores.create(
            name="ItpoBot Vector Store",
        )
    )

    save_vector_store_id(
        vector_store.id
    )

    print(
        f"Created vector store: {vector_store.id}"
    )

    return vector_store.id


if __name__ == "__main__":
    get_or_create_vector_store()