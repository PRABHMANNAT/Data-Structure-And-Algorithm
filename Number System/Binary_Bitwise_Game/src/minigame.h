// minigame.h -- Binary Lock-Pick bonus round.
//
// After certain boss-style enemies the player gets a chest. To open
// it they must reach a target 8-bit pattern from 00000000 by toggling
// individual bit positions. Minimum toggles == popcount(target), and
// achieving that earns a perfect bonus.

#pragma once
#include <cstdint>

namespace br {

// Returns the bonus score awarded (0 on failure).
int playLockPick(uint8_t target);

} // namespace br
