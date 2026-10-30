# Interval Studio — work through the tradeoff

## Predict before running

Can you greedily choose the most valuable booking first?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Load Greedy trap and compare the selected names with the overlap query.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. That booking can block several compatible ones whose combined value is larger.

The central invariant is **Half-open intervals**: [0,2) and [2,4) do not conflict. The related implementation concern is **Augmentation**: Maximum endpoints must be recomputed after every rotation.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Prune overlap searches using maximum ends and half-open boundaries. Use the raw JSON result to check the worked example: A long booking worth 10 loses to two touching bookings worth 8 each: total 16.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: Earliest finish alone solves the unweighted count problem, not arbitrary values. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
