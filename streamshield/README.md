# StreamShield

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
