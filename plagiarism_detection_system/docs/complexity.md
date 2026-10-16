# Complexity

Let `T` be the total token count, `F` the number of selected fingerprints, and
`C` the number of candidate pairs sharing at least one fingerprint. Tokenization,
k-gram hashing, and index insertion are linear in input size in the ordinary case.
The straightforward winnowing implementation scans each window, costing
`O(T × window)` time and `O(F)` selected-fingerprint storage.

Candidate retrieval uses postings from the fingerprint index instead of comparing
all file pairs. For each candidate, set overlap is proportional to fingerprint-set
size. The longest-common-run dynamic program costs up to `O(L²)` time for token
streams capped at 2,000 tokens and `O(L)` memory. Evidence search can also cost
quadratic time for highly repetitive token streams, so large corpora should use
conservative size limits and review the CLI's `--max-bytes` setting.

The detector is intended for modest coursework batches. It is not a distributed
index or a substitute for a specialized large-scale similarity service.
