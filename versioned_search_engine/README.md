# Versioned Search Engine

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Reading room workspace](http://127.0.0.1:8765/versioned_search_engine/web/).

Search your own small document collection with BM25 ranking. Inspect matched terms and autocomplete suggestions.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Transport notes, An empty result.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


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
