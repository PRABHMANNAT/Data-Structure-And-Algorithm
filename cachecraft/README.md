# Cachecraft

Caches trade a bounded set of slots for fewer misses. LRU protects recent keys; LFU protects frequent ones and breaks ties by recency.

## Run

From the repository root, use `python -m cachecraft --example 0`, or `python -m cachecraft --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/cachecraft/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Replay requests in order; every miss inserts the key.
2. Update either the recency list or frequency buckets.
3. Record evictions and compare hit counts on the same trace.

## Worked example

With two slots, a a b c a gives LRU one hit but LFU two: LFU preserves the frequent a.

## Complexity and limits

O(1) amortized access bookkeeping; rendering a full snapshot costs O(capacity).

No. A scan, a hot set and a changing workload reward different policies. This exact educational LFU has no decay; Redis uses different production approximations.

## Verify

Run `python -m unittest discover -s cachecraft/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
