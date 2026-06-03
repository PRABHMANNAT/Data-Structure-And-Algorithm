// bitops.cpp -- implementations of the bitwise primitives.
//
// Each function is a single line; the cast back to uint8_t after a
// shift is important because C++ promotes operands of `<<` and `>>`
// to int, which would otherwise leak garbage into the upper bits.

#include "bitops.h"

namespace br {

uint8_t bAnd(uint8_t a, uint8_t b) { return static_cast<uint8_t>(a & b); }
uint8_t bOr (uint8_t a, uint8_t b) { return static_cast<uint8_t>(a | b); }
uint8_t bXor(uint8_t a, uint8_t b) { return static_cast<uint8_t>(a ^ b); }
uint8_t bNot(uint8_t a)            { return static_cast<uint8_t>(~a); }

uint8_t bShl(uint8_t a, int n) {
    // Clamp the shift amount: shifting by >= width is undefined in C++.
    if (n <= 0) return a;
    if (n >= 8) return 0;
    return static_cast<uint8_t>(a << n);
}

uint8_t bShr(uint8_t a, int n) {
    if (n <= 0) return a;
    if (n >= 8) return 0;
    return static_cast<uint8_t>(a >> n);
}

uint8_t bRotL(uint8_t a, int n) {
    // Rotation: bits that fall off the high end re-enter on the low end.
    n &= 7;
    if (n == 0) return a;
    return static_cast<uint8_t>((a << n) | (a >> (8 - n)));
}

uint8_t bRotR(uint8_t a, int n) {
    n &= 7;
    if (n == 0) return a;
    return static_cast<uint8_t>((a >> n) | (a << (8 - n)));
}

uint8_t setBit(uint8_t v, int pos) {
    return static_cast<uint8_t>(v | (1u << (pos & 7)));
}

uint8_t clearBit(uint8_t v, int pos) {
    return static_cast<uint8_t>(v & ~(1u << (pos & 7)));
}

uint8_t toggleBit(uint8_t v, int pos) {
    return static_cast<uint8_t>(v ^ (1u << (pos & 7)));
}

bool getBit(uint8_t v, int pos) {
    return ((v >> (pos & 7)) & 1u) != 0;
}

} // namespace br
