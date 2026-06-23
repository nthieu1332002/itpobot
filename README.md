### Chunking Strategy

I used OpenAI Vector Store's built-in auto chunking strategy.

The source documents are Zendesk knowledge-base articles that already contain a clear structure (headings, sections, lists, and code blocks). Auto chunking will maintain context while keeping implementation relatively simple.

It will be enough for current data and will provide good retrieval quality without any specific boundaries.

### Indexing Statistics

Uploaded files: 402

Chunk count:
Managed internally by OpenAI File Search and not exposed through the public API.

The project uses OpenAI's built-in chunking pipeline for parsing, chunking, embedding generation, and indexing.
