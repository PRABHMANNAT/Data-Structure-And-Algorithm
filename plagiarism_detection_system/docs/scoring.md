# Scoring

For fingerprint sets `A` and `B`, containment is `|A ∩ B| / min(|A|, |B|)`.
It highlights a short submission embedded in a longer one. Jaccard is
`|A ∩ B| / |A ∪ B|`, which penalizes added material. Sequence overlap is the
longest consecutive normalized-token run divided by the shorter token count.

The displayed score is `0.55 × containment + 0.30 × Jaccard + 0.15 × sequence`,
rounded to four decimals. The default report threshold is 0.35. A pair must share
at least one usable fingerprint and have the same detected language. Scores are
heuristic rankings, not calibrated probabilities or a finding of plagiarism.

The CLI exposes `--threshold`, `--k`, and `--window`. Increasing `k` generally
reduces short coincidental matches but can miss short copied segments. Increasing
the window stores fewer fingerprints and requires longer identical runs.
