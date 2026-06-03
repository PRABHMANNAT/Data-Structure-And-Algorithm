// binary.h -- Binary number-system utilities used by BitRealm.
//
// All gameplay values in the game are 8-bit unsigned integers.
// This module converts between decimal text, binary text, and the
// raw uint8_t representation, plus a few helpers that count bits.

#pragma once
#include <string>
#include <cstdint>

namespace br {

// Format `value` as a fixed-width binary string (MSB first).
// width defaults to 8 because the whole game uses 8-bit registers.
std::string toBinary(uint8_t value, int width = 8);

// Returns the binary string with a space in the middle: "1010 0101".
// Used by the UI so players can read the nibbles at a glance.
std::string toBinaryGrouped(uint8_t value);

// Parse a binary text ("10110001") into a uint8_t. Non-bit chars are
// ignored, which makes it tolerant to spaces or stray punctuation.
uint8_t fromBinary(const std::string& bits);

// Format `value` as "0xAB". Handy in the tutorial and debug prints.
std::string toHex(uint8_t value);

// popcount (number of 1-bits). The game uses this for scoring and
// to display how many bits an attack has cleared.
int countSetBits(uint8_t value);

// True when exactly one bit is set. Used by the lock-pick minigame.
bool isPowerOfTwo(uint8_t value);

} // namespace br
