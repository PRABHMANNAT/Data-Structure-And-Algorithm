# Textloom — work through the tradeoff

## Predict before running

Is a replacement one edit here?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Try repeated lines and inspect one valid shortest script; ties can have different scripts.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. This model counts only insertions and deletions, so replacement costs two edits.

The central invariant is **Edit diagonal**: k=x−y identifies the difference between consumed source and target lines. The related implementation concern is **Snake**: A maximal run of matching lines costs no edits.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Expand edit-distance frontiers until the revised document is reached. Use the raw JSON result to check the worked example: Changing a
b to a
c requires one deletion and one insertion; replacement is not a primitive operation.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: A patch must consume the exact source lines it claims to delete or preserve. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
