// bitops.h -- thin wrappers around every bitwise operation the game uses.
//
// Wrapping the operators in named functions lets the rest of the code
// dispatch through a single `applyWeapon` switch and makes intent
// explicit at call sites (bAnd(hp, mask) reads better than hp & mask
// when nine different ops are in play).

#pragma once
#include <cstdint>

namespace br {

uint8_t bAnd(uint8_t a, uint8_t b);   // a & b
uint8_t bOr (uint8_t a, uint8_t b);   // a | b
uint8_t bXor(uint8_t a, uint8_t b);   // a ^ b
uint8_t bNot(uint8_t a);              // ~a

uint8_t bShl(uint8_t a, int n);       // a << n  (logical left)
uint8_t bShr(uint8_t a, int n);       // a >> n  (logical right)

uint8_t bRotL(uint8_t a, int n);      // rotate left within 8 bits
uint8_t bRotR(uint8_t a, int n);      // rotate right within 8 bits

uint8_t setBit   (uint8_t v, int pos); // v | (1 << pos)
uint8_t clearBit (uint8_t v, int pos); // v & ~(1 << pos)
uint8_t toggleBit(uint8_t v, int pos); // v ^ (1 << pos)
bool    getBit   (uint8_t v, int pos); // (v >> pos) & 1

} // namespace br
