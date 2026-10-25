# StreamShield

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Stream monitor workspace](http://127.0.0.1:8765/streamshield/web/).

Replay event-time data through a sliding window. Inspect late arrivals, the watermark, and heavy hitters.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Late arrival, Steady traffic.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


An event-time stream analytics engine built around bounded-memory data structures.
It combines watermarks, sliding windows, probabilistic frequency estimation, and
deterministic heavy-hitter verification. The project is intentionally dependency-free.

## Highlights

- Strict event-time validation and configurable late-data policies.
- Exact rolling aggregates with amortised O(1) expiry.
- Count-Min Sketch plus Misra-Gries candidate tracking.
- Indexed priority queue for live leaderboards.
- Snapshot/recovery with content checksums.

Run `python -m streamshield --help` after installation.
