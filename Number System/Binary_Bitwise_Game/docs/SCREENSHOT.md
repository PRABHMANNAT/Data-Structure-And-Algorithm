# What a round looks like

(ASCII transcript -- in a real terminal the bit-bars are coloured.)

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
  1) AND Cleaver  [&]   cost=2  -- target = target & mask  (clears bits)
  2) OR Mender    [|]   cost=2  -- self   = self   | mask  (heals/shields)
  3) XOR Bomb     [^]   cost=3  -- target = target ^ mask  (toggles bits)
  4) NOT Strike   [~]   cost=4  -- target = ~target        (full invert)
  5) Left Shift   [<<]  cost=3  -- target = target << n    (amplify/lose MSB)
  6) Right Shift  [>>]  cost=3  -- target = target >> n    (halve, deadly)
  7) Rotate Left  [<<<] cost=3  -- target = rotL(target,n) (wrap-around)
  8) Bit Lance    [=1]  cost=1  -- target = target | (1<<n) (set one bit)
  9) Bit Snap     [=0]  cost=1  -- target = target & ~(1<<n)(clear one bit)
  0) skip turn (regen +3 energy)
  h) help/tutorial
  q) quit to menu
> 1
Enter mask as binary (8 bits, e.g. 11110000) or decimal (0-255): 00001111
Knight HP: 11110000 -> 10000000   (cleared 3 bits)

Knight attacks with mask 00010000.
Your HP: 11111111 -> 11101111
```

Notice how the Knight's shield (`1000 0000`) preserved its top bit
even after the AND tried to clear it.
