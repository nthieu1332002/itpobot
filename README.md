# ItpoBot

A lightweight OptiBot-style knowledge assistant built from OptiSigns Zendesk articles.

## Setup

### Prerequisites

- Python 3.13+
- OpenAI API Key

Create `.env`:

```env
OPENAI_API_KEY=...
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Locally

Run the complete pipeline:

```bash
python main.py
```

The job will:

1. Fetch Zendesk articles
2. Convert HTML to Markdown
3. Detect added/updated articles
4. Upload only changed files to OpenAI Vector Store
5. Update local manifest
6. Generate scrape report

---

## Docker

Build:

```bash
docker build -t itpobot .
```

Run:

```bash
docker run --env-file .env itpobot
```

---

## Chunking Strategy

I used OpenAI Vector Store's built-in auto chunking strategy.

The source documents are Zendesk knowledge-base articles that already contain a clear structure (headings, sections, lists, and code blocks). Auto chunking preserves context while keeping the implementation simple.

No custom chunk boundaries were configured.

---

## Indexing Statistics

- Uploaded files: 402
- Chunk count: Managed internally by OpenAI File Search and not exposed through the public API.

OpenAI handles parsing, chunking, embedding generation, and indexing automatically.

---

## Daily Job Logs

DigitalOcean Job Logs:

---

## Playground Validation

Screenshot:
