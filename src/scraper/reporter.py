import json
from datetime import datetime, timezone
from pathlib import Path

REPORT_PATH = Path(
    "storage/scrape_report.json"
)


def save_scrape_report(
    *,
    total_articles,
    added,
    updated,
    skipped,
):
    REPORT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_articles": total_articles,
        "added": added,
        "updated": updated,
        "skipped": skipped,
    }

    with open(
        REPORT_PATH,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            report,
            f,
            indent=2,
        )