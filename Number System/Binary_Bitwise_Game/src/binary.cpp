// binary.cpp -- implementation of the binary helpers declared in binary.h.

#include "binary.h"
#include <sstream>
#include <iomanip>

namespace br {

std::string toBinary(uint8_t value, int width) {
    // Build the string MSB-first by inspecting one bit at a time.
    std::string out(width, '0');
    for (int i = 0; i < width; ++i) {
        // (1u << i) is the bit-mask for position i.
        // ANDing isolates that one bit; non-zero means it is set.
        if (value & (1u << i)) {
            out[width - 1 - i] = '1';
        }
    }
    return out;
}

std::string toBinaryGrouped(uint8_t value) {
    std::string s = toBinary(value, 8);
    // Split into high and low nibble for readability.
    return s.substr(0, 4) + " " + s.substr(4, 4);
}

uint8_t fromBinary(const std::string& bits) {
    uint8_t result = 0;
    for (char c : bits) {
        if (c == '0' || c == '1') {
            // Standard left-shift accumulation: shift result left,
            // then OR in the new bit.
            result = static_cast<uint8_t>((result << 1) | (c - '0'));
        }
    }
    return result;
}

std::string toHex(uint8_t value) {
    std::ostringstream oss;
    oss << "0x" << std::hex << std::setw(2) << std::setfill('0')
        << static_cast<int>(value);
    return oss.str();
}

int countSetBits(uint8_t value) {
    // Kernighan-style loop: `v & (v-1)` clears the lowest set bit.
    int count = 0;
    while (value) {
        value = static_cast<uint8_t>(value & (value - 1));
        ++count;
    }
    return count;
}

bool isPowerOfTwo(uint8_t value) {
    // A power of two has exactly one bit set, so v & (v-1) == 0.
    return value && !(value & (value - 1));
}

} // namespace br
