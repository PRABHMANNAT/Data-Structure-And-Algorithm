# Joinery

A query planner compares join orders before executing work. Here every subset has an estimated cardinality, and the DP chooses its cheapest left-deep prefix.

## Run

From the repository root, use `python -m joinery --example 0`, or `python -m joinery --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/joinery/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Apply base-table filter selectivities.
2. Enumerate subset masks and append each possible final relation.
3. Reconstruct the cheapest order and compare its cost ledger with input order.

## Worked example

A tiny filtered dimension can reduce intermediate estimates when joined early.

## Complexity and limits

Subset DP O(n²2ⁿ) including cardinality work here; at most eight tables keep enumeration bounded.

No. This is a bounded educational cost model; it does not parse or execute SQL and cannot predict real database latency.

## Verify

Run `python -m unittest discover -s joinery/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
