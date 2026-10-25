# Intermediate Data Structures in Python

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Structure study workspace](http://127.0.0.1:8765/intermediate_data_structures/web/).

Build a search tree from an insertion sequence. Inspect its shape, traversal, and membership.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Balanced branches, A skewed tree.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free learning project implementing practical, intermediate-level data structures from scratch. Each module focuses on clear invariants, predictable errors, and small APIs that are easy to explore.

## Included structures

- Dynamic arrays, singly linked lists, stacks, queues, circular queues, and deques
- Hash maps, binary search trees, binary heaps, and priority queues
- Graphs, tries, and disjoint sets (union-find)

## Quick start

```bash
python -m unittest discover -s intermediate_data_structures/tests -v
python intermediate_data_structures/examples/demo.py
```

The project uses only the Python standard library and targets Python 3.10+.
