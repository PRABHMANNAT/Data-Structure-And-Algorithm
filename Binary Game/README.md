# Binary Quest

Binary Quest is a C++ console game built around decimal and binary conversion.

The game uses only standard C++ libraries and the same core ideas from the number-system examples:

- `% 2` gives the next binary digit.
- `/ 2` moves the decimal number to the next conversion step.
- `pow *= 10` explains place value for learning output.
- `pow *= 2` explains binary-to-decimal place values.

## Aim

The player solves binary missions to unlock gates, collect keys, and open a final vault.

The code is designed to be more interesting than a simple converter, while still keeping the structure easy to read.

## Build And Run

```bash
g++ "binary_quest.cpp" -o binary_quest
./binary_quest
```

On Windows PowerShell:

```powershell
g++ "binary_quest.cpp" -o binary_quest.exe
.\binary_quest.exe
```

Run the built-in checks:

```bash
./binary_quest --self-test
```
