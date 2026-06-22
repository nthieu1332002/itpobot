from src.scraper.reporter import save_scrape_report
from src.scraper.client import ZendeskClient
from src.scraper.markdown_converter import html_to_markdown
from src.scraper.exporter import (
    build_filename,
    build_markdown_document,
    save_markdown,
)

client = ZendeskClient()

articles = client.get_all_articles()

saved_count = 0
failed_count = 0

for article in articles:
    try:
        markdown = html_to_markdown(
            article["body"]
        )

        document = build_markdown_document(
            article,
            markdown,
        )

        filename = build_filename(
            article["title"],
            article["id"]
        )

        save_markdown(
            f"storage/articles/{filename}",
            document,
        )
        
        saved_count += 1

        print(
            f"Saved: {filename}"
        )
    except Exception as e:
        failed_count += 1

        print(
            f"Failed article {article['id']}: {e}"
        )
    
save_scrape_report(
    total_articles=len(articles),
    saved_files=saved_count,
)
print(
    f"Done. Exported {saved_count}/{len(articles)} articles."
)