# Library API

Create `SourceDocument(path, text, language)` values and call
`Detector(DetectorConfig()).compare(documents)`. The result is a descending list
of immutable `Match` objects. A match includes score components, the count of
shared fingerprints, and `Evidence` ranges with source lines.

`DetectorConfig` accepts positive `k`, `window`, `min_shared`, and `max_evidence`
values. `min_score` is between zero and one; `common_fraction` is greater than
zero and at most one. `files.discover(path)` builds documents for the CLI and can
also be used by library callers.

For custom interfaces, `report.to_text`, `report.to_json`, and `report.to_html`
render a match list. The low-level token, fingerprint, index, and similarity
modules are public Python modules for study, but the top-level exports are the
stable entry point for application code.
