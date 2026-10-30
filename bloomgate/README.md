# Bloomgate

Probabilistic structures save memory by allowing specific errors. A Bloom filter may return a false positive; a Count-Min Sketch may overestimate frequency.

## Run

From the repository root, use `python -m bloomgate --example 0`, or `python -m bloomgate --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/bloomgate/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Hash inserts into a shared bitset and several counter rows.
2. Check queries against both structures and exact ground truth.
3. Measure false positives, occupancy and estimated frequency error.

## Worked example

A Bloom answer of absent is definitive after insert-only updates; maybe present requires an exact lookup.

## Complexity and limits

Insert/query O(k + depth), bit memory O(m), counter memory O(width×depth); exact counts are instrumentation only.

No. Other keys can share those bits, so clearing them can introduce false negatives. A counting filter is a different structure.

## Verify

Run `python -m unittest discover -s bloomgate/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
