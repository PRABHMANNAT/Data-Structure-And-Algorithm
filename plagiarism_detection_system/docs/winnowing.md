# Winnowing fingerprints

For each normalized token stream, the detector hashes every consecutive group of `k`
tokens. The `window` parameter controls a second sliding window over those hashes.
Within each window, the smallest hash is selected; ties choose the rightmost position.
Repeated selections are deduplicated by position.

This reduces storage while retaining overlap evidence from sufficiently long common
runs. With `k=5` and `window=4`, any identical run of at least eight normalized tokens
contains a selected fingerprint in both files. The guarantee concerns exact normalized
token runs and assumes the same parameters on both documents. Reordered statements
may still share fragments, but a completely restructured solution need not match.

Hashes use deterministic BLAKE2b output rather than Python's randomized `hash()`, so
reports are reproducible across processes. Hash collisions remain theoretically possible;
the cited token spans should be checked by a reviewer.
