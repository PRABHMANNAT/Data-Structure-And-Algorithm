# Controls

## Main menu

| Key | Action          |
|-----|-----------------|
| 1   | Start Campaign  |
| 2   | Tutorial        |
| 3   | High Scores     |
| 4   | Quit            |

## Combat

| Key | Action                                |
|-----|---------------------------------------|
| 1   | AND Cleaver  -- clear enemy bits      |
| 2   | OR Mender    -- heal yourself         |
| 3   | XOR Bomb     -- flip enemy bits       |
| 4   | NOT Strike   -- invert enemy HP       |
| 5   | Left Shift   -- shift enemy HP <<     |
| 6   | Right Shift  -- shift enemy HP >>     |
| 7   | Rotate Left  -- wrap-around rotate    |
| 8   | Bit Lance    -- set one enemy bit     |
| 9   | Bit Snap     -- clear one enemy bit   |
| 0   | Skip turn (+3 energy regen)           |
| h   | Re-open tutorial                      |
| q   | Quit to main menu                     |

## Entering masks

After picking a weapon you'll be asked for a **mask**. Three formats:

- **8-bit binary string** -- `10110001`
- **Decimal** -- any number from `0` to `255`
- **Bit position** -- a single digit `0-7` (for shifts, rotates,
  Bit Lance and Bit Snap)
