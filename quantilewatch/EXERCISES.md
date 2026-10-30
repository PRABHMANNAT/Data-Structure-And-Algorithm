# Quantile Watch — work through the tradeoff

## Predict before running

Is an IQR flag proof of a fault?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Compare a spike against a constant window and a gradually rising stream.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. It is a statistical signal. A changed distribution can generate flags without a system failure; windows shorter than four are not scored.

The central invariant is **Multiplicity**: Equal keys share a node but each occurrence counts toward rank. The related implementation concern is **Subtree size**: Rotations and deletions must preserve occurrence totals.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Use subtree sizes to select ranks and interpolate quartiles. Use the raw JSON result to check the worked example: For [1,3,5,7], median is 4, Q1 is 2.5 and Q3 is 5.5 under linear interpolation.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: An incoming outlier is judged before it enters the reference window. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
