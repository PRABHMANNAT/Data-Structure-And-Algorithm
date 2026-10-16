# Architecture

The pipeline has five stages: file discovery and text extraction, token normalization,
fingerprinting, candidate lookup, and pairwise scoring. `files.discover` reads
bounded files in sorted order. `ingest` extracts PDF and DOCX text or decodes plain
text. `tokenize.normalize_tokens` removes code comments and formatting,
normalizes identifiers to `ID`, numbers to `NUM`, and strings to `STR`, while retaining
keywords and operators. Its prose profile retains case-folded words.

`fingerprints.kgram_hashes` hashes consecutive token groups with BLAKE2b. `winnow`
retains the rightmost minimum hash in each sliding window, keeping a compact signature
whose positions still point back to source lines. `FingerprintIndex` maps hash values
to document paths, so the engine scores only pairs that share a selected fingerprint.

The engine optionally removes hashes present in most files of a corpus of five or
more submissions. It then combines set overlap and a bounded consecutive-token run.
`evidence.matching_spans` extracts a few nonoverlapping matching ranges. Reports are
rendered as text, JSON, or escaped HTML.
