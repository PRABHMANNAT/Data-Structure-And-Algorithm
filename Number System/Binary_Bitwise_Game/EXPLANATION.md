# BitRealm — Code Explanation

This document walks through every source file in `src/`, explains the
design decisions, and shows exactly how the binary number system and
bitwise operators drive the gameplay.

> If you only read one section, read **§3 Combat math** — it is the
> heart of the game and shows how a single `&`, `|`, `^`, or `~` turns
> into a strategic choice.

---

## Table of contents

1. [High-level architecture](#1-high-level-architecture)
2. [Binary number system layer (`binary.*`)](#2-binary-number-system-layer-binary)
3. [Combat math — the bitwise layer (`bitops.*`)](#3-combat-math--the-bitwise-layer-bitops)
4. [Weapons & dispatch (`weapon.*`)](#4-weapons--dispatch-weapon)
5. [Actors (`player.*`, `enemy.*`)](#5-actors-player-enemy)
6. [Campaign & scoring (`level.*`, `score.*`)](#6-campaign--scoring-level-score)
7. [UI / rendering (`ui.*`)](#7-ui--rendering-ui)
8. [Minigame (`minigame.*`)](#8-minigame-minigame)
9. [Game orchestrator (`game.*`)](#9-game-orchestrator-game)
10. [Entry point (`main.cpp`)](#10-entry-point-maincpp)
11. [Build system (`Makefile`, `build.bat`)](#11-build-system)
12. [Design summary](#12-design-summary)

---

## 1. High-level architecture

```
   main.cpp
      │
      ▼
   Game (game.h/.cpp)
      │       ├── Player        (player.h/.cpp)
      │       ├── Enemy         (enemy.h/.cpp)        ◄── Level (level.h/.cpp)
      │       ├── Weapon[]      (weapon.h/.cpp)
      │       │       │
      │       │       ▼
      │       │   bitops.*  ◄──────────┐
      │       │                        │
      │       ├── UI render (ui.*) ────┘ (uses binary.* + bitops.*)
      │       ├── Minigame (minigame.*)
      │       └── Score (score.*)            ─── scores.txt
      ▼
   stdin / stdout (console)
```

- **`binary.*`** is the *number-system layer*: it converts between
  decimal, binary text, and `uint8_t`. Everything in the game stores
  state as `uint8_t`; only the UI ever touches strings.
- **`bitops.*`** is the *operator layer*: 10 single-line wrappers
  around `&`, `|`, `^`, `~`, shifts, rotates, and single-bit
  set/clear/toggle/get.
- **`weapon.*`** sits on top of `bitops.*` and maps a `Weapon` (a
  player-facing thing with a name, cost, description) to one of those
  operations.
- **`player.*` / `enemy.*`** are the actors. They hold `uint8_t`
  health + a couple of plain ints.
- **`level.*`** is just data — five hand-crafted stages.
- **`ui.*`** does the rendering: bit-bars, banners, ANSI color, the
  Windows ANSI opt-in.
- **`game.*`** glues the rest together: menus, combat loop,
  turn order, shield resolution.
- **`minigame.*`** is a bonus puzzle that exercises `toggleBit`.
- **`score.*`** persists results to a flat text file.

---

## 2. Binary number system layer (`binary.*`)

`src/binary.h` declares six free functions in `namespace br`:

```cpp
std::string toBinary       (uint8_t value, int width = 8);
std::string toBinaryGrouped(uint8_t value);
uint8_t     fromBinary     (const std::string& bits);
std::string toHex          (uint8_t value);
int         countSetBits   (uint8_t value);
bool        isPowerOfTwo   (uint8_t value);
```

### `toBinary`

```cpp
std::string toBinary(uint8_t value, int width) {
    std::string out(width, '0');
    for (int i = 0; i < width; ++i) {
        if (value & (1u << i)) out[width - 1 - i] = '1';
    }
    return out;
}
```

Loops over each bit position `i`, ANDs with the **bit-mask**
`(1u << i)` to isolate that one bit, and writes `'1'` into the
correct position of the output string. The `width - 1 - i` index
is because we want MSB on the left.

This is the canonical "decimal → binary string" routine and is the
basis for every health display in the game.

### `fromBinary`

```cpp
result = (result << 1) | (c - '0');
```

The classic left-shift accumulation: shift the running total one place
left to make room, then OR in the next bit. Skips any character that
isn't `'0'` or `'1'` so the input is forgiving (`"1010 1100"` works).

### `countSetBits` (popcount)

```cpp
while (value) {
    value &= (value - 1);
    ++count;
}
```

**Kernighan's trick.** `v & (v-1)` clears the lowest set bit of `v`,
so the loop runs exactly once per set bit instead of once per bit
position. The UI uses this to label every bit-bar with `bits=N`.

### `isPowerOfTwo`

```cpp
return value && !(value & (value - 1));
```

Same trick: a power of two has exactly one set bit, so after one
Kernighan step the value is zero. The lock-pick uses this to detect
single-bit targets.

---

## 3. Combat math — the bitwise layer (`bitops.*`)

This is where the game *is* the operators. Every wrapper is one line:

```cpp
uint8_t bAnd(uint8_t a, uint8_t b) { return a & b; }
uint8_t bOr (uint8_t a, uint8_t b) { return a | b; }
uint8_t bXor(uint8_t a, uint8_t b) { return a ^ b; }
uint8_t bNot(uint8_t a)            { return ~a;    }
```

So why wrap them? Two reasons:

1. **Dispatch.** `weapon.cpp` has one `switch (op)` that calls the
   right wrapper, so the rest of the game never names a raw operator.
2. **Safety on shifts.** Raw `a << n` promotes `a` to `int`, which can
   leak bits into positions 8-31. The wrappers cast back to `uint8_t`
   and clamp `n` to the legal range:

```cpp
uint8_t bShl(uint8_t a, int n) {
    if (n <= 0) return a;
    if (n >= 8) return 0;
    return static_cast<uint8_t>(a << n);
}
```

`bRotL` / `bRotR` implement an 8-bit rotation by OR-ing the two halves
that fall off either end:

```cpp
uint8_t bRotL(uint8_t a, int n) {
    n &= 7;                            // rotate amount is mod 8
    if (n == 0) return a;
    return (a << n) | (a >> (8 - n));  // wrap the high bits around
}
```

`setBit / clearBit / toggleBit` are textbook:

```cpp
v |   (1u << pos)   // set
v &  ~(1u << pos)   // clear
v ^   (1u << pos)   // toggle
```

`getBit` shifts the target bit down to position 0 and ANDs with 1.

### How a turn resolves

Putting these pieces together, a player turn against an enemy with a
shield runs:

```cpp
uint8_t newHealth = applyWeapon(w, enemy.health, mask);   // raw effect
newHealth =  (newHealth & ~enemy.shield)                  // unshielded bits change
          |  (enemy.health &  enemy.shield);              // shielded bits keep their old value
enemy.health = newHealth;
```

Read line-by-line:

- `~enemy.shield` is the set of bits the player *can* affect.
- `newHealth & ~enemy.shield` keeps the operator's output **only** in
  those positions.
- `enemy.health & enemy.shield` keeps the **original** health bits
  inside the shield mask.
- ORing the two halves splices them together.

This is the same idea as "bitfield masking" you see in low-level C
code, repurposed as a defensive mechanic.

Enemies attack with:

```cpp
playerHealth & ~attackMask
```

i.e. they **clear bits** in your register. To survive you need to keep
some 1-bits alive, which means using `OR Mender` to heal (set bits
back) whenever the attack mask gets close to wiping you.

---

## 4. Weapons & dispatch (`weapon.*`)

```cpp
enum class OpKind { AND, OR, XOR, NOT, SHL, SHR, ROTL, ROTR, SET, CLEAR };

struct Weapon {
    std::string name, symbol, description;
    OpKind      op;
    int         energyCost;
};
```

`applyWeapon` is one `switch` from `OpKind` to a `bitops` call. For
`SHL/SHR/ROTL/ROTR/SET/CLEAR` the user-supplied "mask" is interpreted
as a **bit position** (0-7) instead of an 8-bit mask — the function
masks the input with `& 7` to enforce this.

This decoupling lets `Game::setupArsenal` just initialise a
`std::vector<Weapon>` with literals; adding a new weapon is two lines.

---

## 5. Actors (`player.*`, `enemy.*`)

### `Player`

```cpp
struct Player {
    std::string name;
    uint8_t     health;     // 0 == dead, 0xFF == full
    uint8_t     shield;
    int         energy, maxEnergy;
    int         score, kills;
    // ...
};
```

- `alive()` → `health > 0`. Death is "every bit cleared".
- `heal(mask)` → `health = health | mask`. The classic OR-set trick.
- `spend(cost)` → returns `false` if energy is too low (so the
  combat loop can refuse the action without mutating state).

### `Enemy`

```cpp
struct Enemy {
    std::string name; EnemyKind kind;
    uint8_t     health, shield, attackMask;
    int         rewardScore;
};
```

`makeEnemy(kind)` is a factory with hand-tuned hex patterns:

| Kind    | Health        | Shield     | Attack mask |
|---------|---------------|------------|-------------|
| Goblin  | `0000 1111`   | `0000 0000`| `0000 0001` |
| Knight  | `1111 0000`   | `1000 0000`| `0001 0000` |
| Wizard  | `1010 1010`   | `0000 0010`| `0000 1000` |
| Phantom | `0101 0101`   | `0001 0000`| `0001 0101` |
| Dragon  | `1111 1111`   | `1100 0011`| `0011 1100` |

The patterns are chosen so the player has to *read* the binary to find
the cheapest weapon. e.g. the Goblin has 4 set bits in one nibble, so
`AND 0000 0000` (mask = 0) wipes it in one move — if you can spot it.

`enemyAttack` is `playerHealth & ~attackMask` and that is the entire
AI. Tactically simple; mechanically merciless.

---

## 6. Campaign & scoring (`level.*`, `score.*`)

`Level` is a plain struct of `{ number, title, vector<EnemyKind> }`.
`getLevel(n)` returns the hand-crafted enemy roster for stage `n`. The
campaign is 5 stages long, ending at the Bit Dragon.

`score.cpp` opens `scores.txt` for read or append. Each entry is one
line: `name score levelReached`. `loadScores` parses with
`std::istringstream`; `printTopScores` sorts descending and prints
the top 10. The format is deliberately minimal so the file is easy
to inspect or edit.

---

## 7. UI / rendering (`ui.*`)

The headline helper is `drawBitBar`:

```cpp
void drawBitBar(const std::string& label, uint8_t value, bool useColor) {
    const std::string bits = toBinary(value, 8);
    std::string painted;
    for (char c : bits) {
        painted += (c == '1') ? "\x1b[1;32m1\x1b[0m"   // bright green
                              : "\x1b[90m0\x1b[0m";    // dim gray
    }
    std::cout << label << " [" << painted << "]  "
              << "dec=" << (int)value
              << "  bits=" << countSetBits(value) << '\n';
}
```

It is the only place that paints raw ANSI escapes onto bit characters.
Because the colour codes are 5-7 chars each, the resulting bar is
visually compact while still readable in a plain pipe to a log file
(the escapes degrade to printable garbage but the `dec=` / `bits=`
suffix still tells you the value).

`enableAnsi()` is a Windows-only opt-in:

```cpp
HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
DWORD  mode = 0;
GetConsoleMode(h, &mode);
SetConsoleMode(h, mode | 0x0004);  // ENABLE_VIRTUAL_TERMINAL_PROCESSING
```

Without this, modern Windows Terminal still works (it auto-handles
escapes) but `cmd.exe` on older builds would print `[31m` literally.

---

## 8. Minigame (`minigame.*`)

The lock-pick is a pure exercise in `toggleBit`:

```cpp
for (char c : line) {
    if (c >= '0' && c <= '7') {
        current = toggleBit(current, c - '0');
        ++toggles;
    }
}
```

Reward is `50 + (toggles == popcount(target) ? 50 : 0)`. The perfect
solution is always "toggle exactly the positions that are 1 in the
target", i.e. `popcount(target)` moves — there is no shorter way to
get from `0` to `target` using `toggleBit`. The bonus rewards players
who think before typing.

---

## 9. Game orchestrator (`game.*`)

`Game::run()` is the entry point. It:

1. Calls `enableAnsi()` once.
2. Prints the banner, reads the hero name.
3. Drops into `mainMenu()` which loops on a 4-option prompt.

`startCampaign()` resets `player`, then walks levels 1..5. Each level
calls `playLevel(n)` which walks the enemy list and calls `fight(e)`.

`fight()` is the inner loop:

```cpp
while (player.alive() && enemy.alive()) {
    showStatus(enemy);
    if (!playerTurn(enemy)) continue;     // bad input → re-prompt
    if (!enemy.alive()) return true;      // killed in your turn
    enemyTurn(enemy);
    player.regenEnergy(2);
}
```

### `playerTurn`

Reads a menu choice. `q` quits, `h` re-opens the tutorial, `0` skips
the turn for an energy boost, otherwise it's a weapon index. Cost is
paid up front via `player.spend(cost)`; on insufficient energy the
turn is rejected and the player keeps their energy.

The shield resolution (covered in §3) lives here.

### `enemyTurn`

A single call:

```cpp
player.takeDamage(enemyAttack(enemy, player.health));
```

Then a diagnostic print showing the before/after bit-bars.

### `readMask`

The trickiest UX bit. It accepts:

- An 8-character binary string of 0s and 1s → parsed with
  `fromBinary`.
- A decimal `0-255` → `std::stoi`, clamped.

For shift/rotate/set/clear weapons the prompt explicitly asks for a
position 0-7. The function returns `uint8_t`, so even a decimal `300`
is silently clamped — defensive but not chatty.

---

## 10. Entry point (`main.cpp`)

```cpp
#include "game.h"
int main() { br::Game g; g.run(); return 0; }
```

Five lines. All real work is in `Game::run()` so the entry point is
trivial and testable.

---

## 11. Build system

### `Makefile`

```
CXXFLAGS := -std=c++17 -Wall -Wextra -O2 -Isrc
SRC      := $(wildcard src/*.cpp)
OBJ      := $(SRC:.cpp=.o)
TARGET   := bitrealm
```

A 15-line POSIX `Makefile` — globs `src/*.cpp`, compiles each,
links into `bitrealm`. Targets: `all`, `clean`, `run`.

### `build.bat`

One `g++` invocation that globs `src\*.cpp` and produces
`bitrealm.exe`. Designed for the MinGW toolchain on Windows, which is
the most common setup in the parent course.

Both build paths are dependency-free — no CMake, no vcpkg, no
package manager. Open a terminal, run one command, get an executable.

---

## 12. Design summary

What did we get out of just two concepts?

- **Binary representation** → 8-bit health registers, score patterns,
  attack masks, lock-pick targets, all stored as `uint8_t`.
- **Bitwise operators** → every gameplay action (attack, heal, shield
  bypass, lock-pick, enemy AI) is one of the 10 wrappers in
  `bitops.cpp`.

The "interesting" gameplay falls out automatically: an attack mask of
`11111111` would be game-over in one move, but the AND/OR/XOR weapons
let you erode it strategically. The shield mechanic teaches the
**bitfield masking idiom** (`(new & ~shield) | (old & shield)`) by
making it the central tactical puzzle.

There is intentionally **no arithmetic** in combat — no subtraction
of HP, no random rolls. Damage is whatever the bit pattern after the
operator becomes. That constraint is what makes the game worth the
"binary + bitwise" label.
