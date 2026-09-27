# Design decisions

This project chooses exact window sums and approximate all-time frequencies. That
split makes customer-visible totals deterministic while bounding the memory used by
high-cardinality keys. Candidate tracking prevents the leaderboard from scanning every key.
