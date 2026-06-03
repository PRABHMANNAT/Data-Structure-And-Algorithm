# Strategy tips

A short cheat-sheet of bitwise habits that win fights.

## Read the bits before you pick a weapon

The bit-bar shows you the enemy's HP every round. Count the 1-bits
(the `bits=N` label after the bar). That number is your "real" health
target -- you need to clear every 1.

## One-shot wipes

If the enemy's HP can be cleared by a single mask, **just AND with the
complement**:

```
enemy HP   = 0000 1111
AND with   = 0000 0000
result     = 0000 0000   <- dead
```

Goblins (`0000 1111`) die in one AND-with-0. Always check for this
first; it costs 2 energy and saves the round.

## Use XOR as a precision tool

XOR with a pattern *equal* to the enemy's HP flips every bit to its
opposite: same-bit XOR = 0. So `XOR 1010 1010` on a Wizard wipes them
in one move -- and chips their shield bit at the same time.

## The shield is not a wall, it's a delay

Shielded bits are immune to direct ops. But XOR also peels the shield
(`shield = shield & ~mask`), so two XOR bombs in a row often shred a
Dragon's `1100 0011` shield enough to land a finishing AND.

## OR Mender = patch holes, not full heal

OR-heal sets bits, it never clears them. So if your HP is `1110 1110`
the Mender can restore the gaps with `OR 0001 0001`. You can't go
above `1111 1111`, so don't waste energy on already-set bits.

## Right Shift is sneaky strong

`HP >> 1` halves the enemy's value and drops the lowest set bit.
Against a high-nibble enemy like the Knight (`1111 0000`), three
right-shifts wipe them outright.

## NOT Strike is feast or famine

NOT is the most expensive operator (4 energy). It's brilliant when
the enemy's HP is *mostly 1s* (because most bits go to 0), and awful
when it's mostly 0s (you just gave them HP). Save it for the Dragon.

## Energy economy

You regen +2 each round and +4 each level. Skipping a turn is +3.
The 1-energy weapons (Bit Lance, Bit Snap) are cheap chip damage when
you are broke; don't burn 3 energy on a XOR Bomb if a single
`CLEAR bit 3` finishes the job.
