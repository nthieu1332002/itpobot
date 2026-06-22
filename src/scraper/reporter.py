import json
from pathlib import Path
from datetime import datetime, timezone


def save_scrape_report(
    total_articles: int,
    saved_files: int,
):
    report = {
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "total_articles": total_articles,
        "saved_files": saved_files,
    }

    Path("storage").mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        "storage/scrape_report.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            report,
            f,
            indent=2,
        )