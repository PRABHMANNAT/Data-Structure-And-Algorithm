# Shard Ring

A placement function should move only a subset of keys when membership changes. Virtual nodes smooth a ring; weighted rendezvous scores each server independently.

## Run

From the repository root, use `python -m shardring --example 0`, or `python -m shardring --input payload.json`. Only the Python standard library is needed. The JSON schema and three runnable workloads are in [web/project.json](web/project.json).

Start `python -m workbench.server` and open [the browser demo](http://127.0.0.1:8765/#project/shardring/demo). Its input form runs this same service; the result can be exported as JSON, compared with a previous run, or explored through the visual result.

## Implementation

`models.py` defines the domain records, `parse.py` validates bounded input, `core.py` implements the primary structure, `extra.py` adds the second algorithm, and `service.py` composes the result. `__main__.py` is a JSON CLI; `web/adapter.py` calls the same service.

1. Place weighted virtual nodes on a stable hash ring.
2. Assign each key clockwise and independently with a weighted rendezvous race.
3. Add one server and compare old/new owners and distinct replica preferences.

## Worked example

With one original server, adding a second moves only keys now owned by the newcomer.

## Complexity and limits

Ring lookup O(log tokens); rendezvous O(servers) per key; replica enumeration can scan tokens.

No. Weight describes expected distribution over many keys; small samples can be uneven.

## Verify

Run `python -m unittest discover -s shardring/tests -v` from the repository root. Core tests cover invariants and boundary cases; oracle tests compare against a separate slow reference. HTTP adapter tests are included in `python scripts/verify.py --web`.

See [EXERCISES.md](EXERCISES.md) for a guided experiment and solution.
