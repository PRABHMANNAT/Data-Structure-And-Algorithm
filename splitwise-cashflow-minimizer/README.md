# Splitwise Cashflow Minimizer

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Settle up workspace](http://127.0.0.1:8765/splitwise-cashflow-minimizer/web/).

Turn shared expenses into net balances and a compact settlement plan. Every amount stays in integer cents.

The interface runs the native C++ implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Weekend away, Uneven cents.

A C++20 compiler must be available as `g++` or through the `CXX` environment variable. The server builds the checked-in bridge on first run.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A C++20 command-line program that reduces a list of group expenses into the smallest practical set of payments. It calculates net balances, then uses creditor and debtor max-heaps to settle the largest obligations first.

## Cent allocation

Equal splits use whole cents. If an amount does not divide evenly, participants are sorted alphabetically and the first participants receive one extra cent of the expense until the remainder is allocated. For example, 100 cents shared by Ada, Ben, and Cam allocates 34, 33, and 33 cents. Duplicate participant names are rejected. The greedy heap reduces transfers but does not guarantee the global minimum number.

## Run

```bash
cmake -S . -B build
cmake --build build
./build/splitwise examples/weekend.csv
```
