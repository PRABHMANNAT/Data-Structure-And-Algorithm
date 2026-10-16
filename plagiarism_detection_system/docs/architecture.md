# Architecture

The pipeline has five stages: file discovery, token normalization, fingerprinting,
candidate lookup, and pairwise scoring. `files.discover` reads bounded UTF-8 source
files in sorted order. `tokenize.normalize_tokens` removes comments and formatting,
normalizes identifiers to `ID`, numbers to `NUM`, and strings to `STR`, while retaining
keywords and operators.

`fingerprints.kgram_hashes` hashes consecutive token groups with BLAKE2b. `winnow`
retains the rightmost minimum hash in each sliding window, keeping a compact signature
whose positions still point back to source lines. `FingerprintIndex` maps hash values
to document paths, so the engine scores only pairs that share a selected fingerprint.

The engine optionally removes hashes present in most files of a corpus of five or
more submissions. It then combines set overlap and a bounded consecutive-token run.
`evidence.matching_spans` extracts a few nonoverlapping matching ranges. Reports are
rendered as text, JSON, or escaped HTML.
