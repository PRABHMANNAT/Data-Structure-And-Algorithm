# GraphForge

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Network atlas workspace](http://127.0.0.1:8765/graphforge/web/).

Explore versioned directed graphs. Find a weighted route and inspect an earlier revision of the network.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Across town, An isolated destination, Before the shortcut.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


GraphForge is a dependency-free Python toolkit for versioned routing networks.
It focuses on algorithms that production routing services actually need: immutable
revisions, transactional edits, shortest-path strategies, constrained search, and
deterministic algorithm diagnostics.

## Highlights

- Copy-on-write graph revisions with cheap read isolation.
- Dijkstra and A* with admissible-heuristic checks.
- K-shortest simple routes, strongly connected components, and topological analysis.
- Rollback union-find for offline connectivity queries.

Run `python -m graphforge --help` after installation.
