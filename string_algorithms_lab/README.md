# String Algorithms Lab

A dependency-free Python project for learning exact matching, multi-pattern search, suffix indexes, and sequence dynamic programming. It includes a JSON CLI, a runnable demo, and cross-check tests.

## Run

Requires Python 3.10 or newer. From this directory:

```bash
python -m unittest discover -s tests -v
python -m examples.demo
python -m stringlab search bananana ana --algorithm kmp
python -m stringlab multi ushers he she his hers
python -m stringlab suffix banana ana
python -m stringlab palindrome babad
```

You can also install the local package with `python -m pip install -e .` and use the `stringlab` command.

## API

```python
from stringlab.api import search, compare
from stringlab.aho_corasick import AhoCorasick
from stringlab.streaming_kmp import KMPStream
from stringlab.suffix_search import SuffixIndex

assert search("banana", "ana").positions == (1, 3)
assert AhoCorasick(["ana", "na"]).find_all("banana") == {"ana": [1, 3], "na": [2, 4]}
assert SuffixIndex("banana").find_all("ana") == [1, 3]

stream = KMPStream("ana")
assert stream.feed("ban") == []
assert stream.feed("ana") == [1, 3]
```

Exact search methods use code-point offsets, include overlapping matches, and return every boundary for an empty pattern. Streaming and multi-pattern matchers require nonempty patterns. See [algorithms](docs/algorithms.md) and [complexity](docs/complexity.md) for the tradeoffs.
