# Enemy roster

All values are 8-bit. Patterns are chosen so each enemy rewards a
different bitwise tactic.

| Enemy   | HP            | Shield      | Attack mask  | Reward | Best counter                        |
|---------|---------------|-------------|--------------|--------|-------------------------------------|
| Goblin  | `0000 1111`   | `0000 0000` | `0000 0001`  | 50     | `AND 0x00` wipes in one move        |
| Knight  | `1111 0000`   | `1000 0000` | `0001 0000`  | 120    | `Right Shift` to drop low bits, then chip the shield with `XOR` |
| Wizard  | `1010 1010`   | `0000 0010` | `0000 1000`  | 180    | `AND 0101 0101` clears all real HP  |
| Phantom | `0101 0101`   | `0001 0000` | `0001 0101`  | 220    | `XOR 0101 0101` toggles HP to 0; mind the shield bit |
| Dragon  | `1111 1111`   | `1100 0011` | `0011 1100`  | 500    | Use `XOR` to peel the shield, then `AND 0000 0000` for the kill blow |

## Boss drop

Knights drop a **Binary Lock-Pick** chest. The target pattern is
`attackMask | 0b01000010`. Open it with the fewest possible toggles
(equal to `popcount(target)`) to earn the perfect bonus.
