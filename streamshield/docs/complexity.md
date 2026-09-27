# Complexity

| Operation | Complexity | Memory |
| --- | --- | --- |
| Ingest | O(log h + d) | O(w + d/epsilon) |
| Window expiry | amortised O(1) per event | O(w) |
| Frequency estimate | O(d) | O(d/epsilon) |

`h` is active leaderboard keys, `d` sketch depth, and `w` events retained.
