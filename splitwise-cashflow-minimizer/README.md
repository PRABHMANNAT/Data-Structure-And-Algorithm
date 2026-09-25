# Splitwise Cashflow Minimizer

A C++20 command-line program that reduces a list of group expenses into the smallest practical set of payments. It calculates net balances, then uses creditor and debtor max-heaps to settle the largest obligations first.

## Run

```bash
cmake -S . -B build
cmake --build build
./build/splitwise examples/weekend.csv
```
