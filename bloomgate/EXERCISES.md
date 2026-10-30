# Bloomgate — work through the tradeoff

## Predict before running

Can I delete a key by clearing its Bloom bits?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Use Collision pressure and compare actual counts against estimates.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. Other keys can share those bits, so clearing them can introduce false negatives. A counting filter is a different structure.

The central invariant is **One-sided error**: Inserted keys cannot become false negatives without deletion or corruption. The related implementation concern is **Counter collisions**: Nonnegative updates mean sketch estimates cannot undercount.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Check queries against both structures and exact ground truth. Use the raw JSON result to check the worked example: A Bloom answer of absent is definitive after insert-only updates; maybe present requires an exact lookup.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: The standard FPR formula is an approximation, not a guarantee on this query sample. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
