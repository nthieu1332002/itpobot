import requests

class ZendeskClient:
    BASE_URL = "https://support.optisigns.com"

    def get_articles_page(self, page: int = 1):
        url = (
            f"{self.BASE_URL}"
            f"/api/v2/help_center/en-us/articles.json?page={page}"
        )

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        return response.json()

    def get_all_articles(self):
        all_articles = []

        page = 1

        while True:
            data = self.get_articles_page(page)

            articles = data["articles"]

            all_articles.extend(articles)

            print(
                f"Fetched page {page}: "
                f"{len(articles)} articles"
            )

            if data["next_page"] is None:
                break

            page += 1

        return all_articles