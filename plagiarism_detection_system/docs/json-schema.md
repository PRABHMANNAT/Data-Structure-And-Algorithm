# JSON report shape

JSON output has one top-level `matches` array. Each match contains `left` and `right`
paths, a blended `score`, component values `containment`, `jaccard`, and `sequence`,
the `shared_fingerprints` count, and an `evidence` array. Evidence entries contain
token offsets `left_start` and `right_start`, `length`, and one-based source lines
`left_line` and `right_line`.

The paths are the absolute paths returned by file discovery. Library callers can
provide their own stable path labels. Scores are numbers from zero through one.
The evidence list is capped, sorted by longest span first, and may be empty when
the files share fingerprints but no span meets the current `k` threshold.

Consumers should treat this as an inspection format and retain their own submission
metadata separately. They should not interpret a missing pair as proof of originality.
