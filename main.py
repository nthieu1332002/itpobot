from src.scraper.client import (
    ZendeskClient,
)

from src.scraper.markdown_converter import (
    html_to_markdown,
)

from src.scraper.exporter import (
    build_filename,
    build_markdown_document,
    save_markdown,
)

from src.scraper.manifest import (
    load_manifest,
    save_manifest,
    detect_change,
    build_article_hash,
)

from src.scraper.reporter import (
    save_scrape_report,
)

from src.assistant.upload_files import (
    upload_files,
)


client = ZendeskClient()

articles = client.get_all_articles()

manifest = load_manifest()

added = 0
updated = 0
skipped = 0

uploaded_files = []

for article in articles:

    try:
        status = detect_change(
            article,
            manifest,
        )

        if status == "skipped":
            skipped += 1
            continue

        markdown = html_to_markdown(
            article["body"]
        )

        document = (
            build_markdown_document(
                article,
                markdown,
            )
        )

        filename = build_filename(
            article["title"],
            article["id"],
        )

        filepath = (
            f"storage/articles/{filename}"
        )

        save_markdown(
            filepath,
            document,
        )

        uploaded_files.append(
            filepath
        )

        manifest[
            str(article["id"])
        ] = {
            "hash": build_article_hash(
                article
            ),
            "updated_at": article[
                "updated_at"
            ],
        }

        if status == "added":
            added += 1

        elif status == "updated":
            updated += 1

        print(
            f"{status.upper()} -> {filename}"
        )

    except Exception as e:

        print(
            f"Failed article {article['id']}: {e}"
        )

batch = upload_files(
    uploaded_files
)

if (
    batch is None
    or batch.status == "completed"
):
    save_manifest(
        manifest
    )
else:
    raise Exception(
        "Upload failed"
    )
    
save_scrape_report(
    total_articles=len(
        articles
    ),
    added=added,
    updated=updated,
    skipped=skipped,
)

print()

print(
    f"Added: {added}"
)

print(
    f"Updated: {updated}"
)

print(
    f"Skipped: {skipped}"
)