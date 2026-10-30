# Spatial Desk — work through the tradeoff

## Predict before running

Does a KD tree guarantee logarithmic queries?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Use Equal distances, then set the radius to exactly one.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. Its performance depends on dimension and geometry; worst-case search still visits every point.

The central invariant is **Squared distance**: Comparisons avoid square roots until display. The related implementation concern is **Branch and bound**: A lower bound rejects regions that cannot improve the answer.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Search the nearer branch and maintain the best k points in a max-heap. Use the raw JSON result to check the worked example: Four points one unit from the origin tie on distance; names break ties deterministically.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: Equal coordinates and large k can force a nearly full scan. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
