# BitRealm — Binary Battle Arena

A turn-based C++ console game where **everything is 8 bits** and **every
action is a bitwise operation**. Reduce each enemy's health register to
`00000000` before yours hits zero. No arithmetic damage formulas, no hit
dice — just `&`, `|`, `^`, `~`, `<<`, `>>`, rotates, and single-bit
set/clear.

Built around two and only two concepts from this DSA repo:

1. **Binary number system** (8-bit registers, decimal/binary/hex views)
2. **Bitwise operators** (`AND`, `OR`, `XOR`, `NOT`, `SHL`, `SHR`,
   rotates, and bit set/clear/toggle/get)

---

## Quick start

### Windows (MinGW / g++)
```bat
build.bat
bitrealm.exe
```

### Linux / macOS / WSL
```sh
make
./bitrealm
```

You need any modern C++17 compiler. There are no external dependencies.

---

## What you actually do in the game

Every turn you pick a weapon from your arsenal. A weapon is just a
named bitwise operation:

| Weapon         | Op    | Effect                                |
|----------------|-------|---------------------------------------|
| AND Cleaver    | `&`   | `enemyHP = enemyHP & mask`            |
| OR Mender      | `\|`  | `selfHP  = selfHP  \| mask`  (heal)   |
| XOR Bomb       | `^`   | `enemyHP = enemyHP ^ mask`            |
| NOT Strike     | `~`   | `enemyHP = ~enemyHP`                  |
| Left Shift     | `<<`  | `enemyHP = enemyHP << n`              |
| Right Shift    | `>>`  | `enemyHP = enemyHP >> n`              |
| Rotate Left    | `<<<` | wrap-around rotate                    |
| Bit Lance      | `=1`  | set one bit                           |
| Bit Snap       | `=0`  | clear one bit                         |

Then you type a **mask**: either an 8-bit binary string (`11110000`)
or a decimal `0-255`. The game shows you the before/after bit pattern
every round, so you can see exactly what your operator did.

Enemies fight back by **clearing bits** from your health
(`yourHP & ~attackMask`). Some enemies wear **shields**: bits inside
their shield mask are immune to direct modification. Use `XOR` to chip
away at the shield first.

A boss-style Knight drops a **Binary Lock-Pick** minigame: reach the
target pattern by toggling individual bit positions, in as few moves
as possible.

---

## A round at the table

```
=== LEVEL 2: Iron Bastion ===

A wild Knight appears!

--- Round 1 ---

Hero HP [11111111]  dec=255  bits=8
Energy: 8/8   Score: 50

Knight  HP [11110000]  dec=240  bits=4
  Shield  [10000000]  dec=128  bits=1
  Attack mask: 00010000

Arsenal:
  1) AND Cleaver  [&]   cost=2  -- target = target & mask
  2) OR Mender    [|]   cost=2  -- self   = self   | mask
  3) XOR Bomb     [^]   cost=3  -- target = target ^ mask
  ...
> 1
Enter mask as 8-bit binary or decimal: 00001111
Knight HP: 11110000 -> 10000000   (AND, cleared 3 bits)

Knight attacks with mask 00010000.
Your HP: 11111111 -> 11101111
```

Notice the Knight's shield (`1000 0000`) preserved its top bit even
after the AND tried to clear it. That is the central tactical wrinkle.

---

## Project layout

```
Binary_Bitwise_Game/
├── README.md           <- you are here
├── EXPLANATION.md      <- full code walk-through, file by file
├── CHANGELOG.md
├── Makefile            <- POSIX build
├── build.bat           <- Windows build
├── docs/
│   ├── CONTROLS.md
│   ├── ENEMIES.md
│   ├── SCREENSHOT.md
│   └── TIPS.md
└── src/
    ├── main.cpp        <- entry point
    ├── game.{h,cpp}    <- orchestrator, menus, combat loop
    ├── player.{h,cpp}  <- player state
    ├── enemy.{h,cpp}   <- enemy roster + AI
    ├── weapon.{h,cpp}  <- arsenal & dispatch
    ├── level.{h,cpp}   <- 5-stage campaign
    ├── score.{h,cpp}   <- on-disk high scores
    ├── ui.{h,cpp}      <- ANSI colors, banners, bit-bars
    ├── minigame.{h,cpp}<- binary lock-pick
    ├── bitops.{h,cpp}  <- the 10 bitwise primitives
    └── binary.{h,cpp}  <- dec/bin/hex helpers, popcount
```

See [EXPLANATION.md](./EXPLANATION.md) for a deep dive into how each
file works and the design choices behind the combat math.

---

## Controls (in combat)

| Key  | Action                                            |
|------|---------------------------------------------------|
| 1-9  | Pick weapon                                       |
| 0    | Skip turn (+3 energy regen)                       |
| h    | Re-open the binary/bitwise tutorial               |
| q    | Quit to main menu                                 |

When the game asks for a mask you may type:
- a binary string of 8 bits, e.g. `10110001`
- a decimal `0-255`, e.g. `177`
- for shift/rotate/set/clear: a single digit `0-7` (bit count/position)

Full key reference: [docs/CONTROLS.md](./docs/CONTROLS.md).
Strategy hints: [docs/TIPS.md](./docs/TIPS.md).

---

## Why this exists

This is a portfolio / coursework piece for the
**Data-Structure-And-Algorithm / Number System** track. The aim is to
take two textbook concepts (binary representation + bitwise operators)
and stretch them into a complete, playable, well-organised C++ program
that demonstrates the operators in actual use rather than as
five-line snippet exercises.
