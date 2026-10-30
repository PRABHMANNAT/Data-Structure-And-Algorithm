# Flow Foundry — work through the tradeoff

## Predict before running

Can opposite input edges share the same reverse arc?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Run Parallel pipes and verify conservation at a.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. Original antiparallel and parallel edges need separate residual pairs to preserve capacities and flow accounting.

The central invariant is **Residual capacity**: How much additional flow an arc can carry. The related implementation concern is **Reverse edge**: Allows existing flow to be canceled when rerouting.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Use BFS levels and blocking-flow DFS until the sink is unreachable. Use the raw JSON result to check the worked example: s→a capacity 7 and a→t capacity 4 carry at most 4 units; the final cut has capacity 4.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: A cut with capacity equal to the feasible flow certifies optimality. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
