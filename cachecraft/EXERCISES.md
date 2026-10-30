# Cachecraft — work through the tradeoff

## Predict before running

Is LFU always better?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Compare a hot key followed by a completely new working set.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. A scan, a hot set and a changing workload reward different policies. This exact educational LFU has no decay; Redis uses different production approximations.

The central invariant is **Intrusive list**: A map points directly to linked-list nodes, avoiding scans. The related implementation concern is **Frequency buckets**: Each bucket orders keys with equal frequency by recency.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Update either the recency list or frequency buckets. Use the raw JSON result to check the worked example: With two slots, a a b c a gives LRU one hit but LFU two: LFU preserves the frequent a.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: An exact LFU without aging can protect yesterday’s hot keys. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
