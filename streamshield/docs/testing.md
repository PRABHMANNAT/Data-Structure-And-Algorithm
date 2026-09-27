# Testing strategy

Unit tests cover each data structure's local invariant. Integration tests should
exercise disorder, late arrivals, and a long expiry run. Property tests are useful
for heap index consistency and sketch monotonicity.
