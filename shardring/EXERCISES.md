# Shard Ring — work through the tradeoff

## Predict before running

Does a three-times weight guarantee three-times these sample keys?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Change virtual nodes from one to 32 while keeping the exact same keys.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. Weight describes expected distribution over many keys; small samples can be uneven.

The central invariant is **Virtual nodes**: More tokens reduce but do not eliminate imbalance. The related implementation concern is **Stable hashing**: SHA-256 gives deterministic placement across Python processes.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Assign each key clockwise and independently with a weighted rendezvous race. Use the raw JSON result to check the worked example: With one original server, adding a second moves only keys now owned by the newcomer.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: Unchanged servers retain their pairwise rendezvous order. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
