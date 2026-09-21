# Versioned Search Engine

A dependency-free Python search engine implemented as a DSA project. It supports document indexing, Boolean and phrase queries, BM25 ranking, prefix completion, snapshot history, and link-based recommendations.

## Features

- Positional inverted index for phrase matching
- Trie autocomplete, Boolean set operations, and BM25 ranking
- LRU cache invalidation, snapshots, Bloom-filter deduplication, and graph recommendations
- JSON corpus import/export, CLI search, fixtures, and unit tests

## Run

```bash
python -m unittest discover -s versioned_search_engine/tests -t versioned_search_engine -v
python versioned_search_engine/examples/demo.py
```
