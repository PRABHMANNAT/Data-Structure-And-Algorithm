# Number notebook

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Number notebook workspace](http://127.0.0.1:8765/Number%20System/web/).

Convert signed decimal integers into binary and inspect every division step.

The interface runs the native C++ implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Forty-two, Zero, Negative input.

A C++20 compiler must be available as `g++` or through the `CXX` environment variable. The server builds the checked-in bridge on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.
