# Joinery — work through the tradeoff

## Predict before running

Is this the actual PostgreSQL optimizer?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Load Selective dimension and compare both cost ledgers.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. This is a bounded educational cost model; it does not parse or execute SQL and cannot predict real database latency.

The central invariant is **Optimal substructure**: The best order for a subset can extend the best prefix under this additive model. The related implementation concern is **Cardinality estimation**: Independent predicate selectivities are an assumption, not measured row counts.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Enumerate subset masks and append each possible final relation. Use the raw JSON result to check the worked example: A tiny filtered dimension can reduce intermediate estimates when joined early.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: Only left-deep plans are considered; physical join methods and bushy trees are excluded. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
