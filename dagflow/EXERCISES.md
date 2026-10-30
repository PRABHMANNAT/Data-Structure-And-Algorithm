# DAGflow — work through the tradeoff

## Predict before running

Does zero slack mean a worker is always busy?

Write down a prediction before opening the result. Use the starter example, then change just one input.

## Experiment

Reduce workers from two to one and compare the critical bound with the actual schedule.

Record the original input, changed input and both outputs. Identify a correctness invariant separately from a performance expectation.

## Explanation

No. Slack is computed from dependencies alone. Actual resource contention can create additional waiting.

The central invariant is **Topological order**: Every predecessor appears before its dependent. The related implementation concern is **Slack**: Latest start minus earliest start under unlimited resources.

## Follow the source

Trace the call from `service.run` through `parse`, then locate the decision described in step 2: Compute earliest/latest times to identify zero-slack critical tasks. Use the raw JSON result to check the worked example: Two independent tasks lasting 4 and 3 finish in 4 with two workers, but 7 with one.

## Stretch task

Create a counterexample to an overly strong guarantee. Explain why this boundary matters: Limited-worker list scheduling is deterministic but not globally optimal. Compare your reasoning with the independent reference in `tests/test_oracle.py` before changing the implementation.
