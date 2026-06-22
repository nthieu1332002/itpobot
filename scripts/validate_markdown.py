import frontmatter
from pathlib import Path

errors = []

files = list(
    Path("storage/articles").glob("*.md")
)

for file in files:
    try:
        post = frontmatter.load(file)

        metadata = post.metadata

        if not metadata.get("title"):
            raise ValueError("missing title")

        if not metadata.get("article_id"):
            raise ValueError("missing article_id")

        if not metadata.get("url"):
            raise ValueError("missing url")

        if not post.content.strip():
            raise ValueError("empty content")

    except Exception as e:
        errors.append(
            f"{file.name}: {e}"
        )

print(
    f"Checked {len(files)} files"
)

print(
    f"Errors: {len(errors)}"
)

if errors:
    print("\nValidation Errors:")

    for error in errors:
        print(error)