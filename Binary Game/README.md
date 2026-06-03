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

## Mission Types

1. Decimal to binary gate
2. Binary to decimal decoder
3. Missing-bit repair
4. Power-of-two gate
5. Binary place-value challenge
6. Final vault binary code

Each correct answer gives a key. Wrong answers reduce health. A streak gives bonus score, so correct answers in a row matter.

## How The Core Conversion Works

For decimal to binary, the game uses this idea:

```cpp
while (number > 0) {
    int rem = number % 2;
    binary.push_back('0' + rem);
    number /= 2;
}
```

The digits are collected from right to left, so the program reverses them at the end.

For binary to decimal, the game reads from right to left:

```cpp
if (binary[i] == '1') {
    answer += pow;
}
pow *= 2;
```

That means the places are `1, 2, 4, 8, 16...`.
