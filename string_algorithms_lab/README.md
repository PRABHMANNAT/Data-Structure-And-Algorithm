# String Algorithms Lab

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Pattern bench workspace](http://127.0.0.1:8765/string_algorithms_lab/web/).

Find every occurrence of a pattern. Cross-check five exact matchers and inspect overlapping matches.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Overlapping matches, Repeated prefix.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


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
