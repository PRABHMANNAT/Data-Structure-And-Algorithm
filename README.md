# Data Structure And Algorithm

This repository contains C++ programs for data structure and algorithm practice.

## Programs

- `Number System/decimal_to_binary.cpp` - Converts a decimal integer to binary.
- `Number System/decimal_to_binary_place_value.cpp` - Converts a non-negative decimal number to binary using the remainder and place-value method.
- `Binary Game/binary_quest.cpp` - A C++ console game that teaches decimal and binary conversion through missions.

## Explanation

The place-value method divides the decimal number by `2` repeatedly, stores each remainder, and places it into the answer using `pow`.

For `50`:

```text
50 % 2 = 0
25 % 2 = 1
12 % 2 = 0
 6 % 2 = 0
 3 % 2 = 1
 1 % 2 = 1
```

Reading the remainders from bottom to top gives:

```text
50(decimal) = 110010(binary)
```

In the code:

- `% 2` gives the next binary digit.
- `/ 2` moves to the next step.
- `pow *= 10` moves to the next output position.
- `ans` builds the final binary-looking number.

This method is mainly for learning because large answers can overflow numeric types. For large numbers, storing the binary result as a `string` is better.

## Run

```bash
g++ "Number System/decimal_to_binary.cpp" -o decimal_to_binary
./decimal_to_binary

g++ "Number System/decimal_to_binary_place_value.cpp" -o decimal_to_binary_place_value
./decimal_to_binary_place_value

g++ "Binary Game/binary_quest.cpp" -o binary_quest
./binary_quest
```
