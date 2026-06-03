// weapon.h -- the player's arsenal.
//
// Every weapon is just a labelled bitwise operation. The Game class
// owns a vector<Weapon> and the player chooses one each turn.

#pragma once
#include <string>
#include <cstdint>

namespace br {

// Each enum value maps 1:1 to a function in bitops.h.
enum class OpKind {
    AND, OR, XOR, NOT,
    SHL, SHR, ROTL, ROTR,
    SET, CLEAR
};

struct Weapon {
    std::string name;        // shown in the arsenal menu
    std::string symbol;      // short glyph e.g. "&", "^"
    OpKind      op;          // which bitwise op to apply
    int         energyCost;  // how much energy the player spends
    std::string description; // one-liner shown in the menu
};

// Apply weapon `w` to `target` using `mask`. For NOT, mask is ignored.
// For shift / rotate / set / clear the mask is interpreted as a bit
// position (0-7); for AND/OR/XOR it is a full 8-bit mask.
uint8_t applyWeapon(const Weapon& w, uint8_t target, uint8_t mask);

// Human-readable name of the operator, used in trace messages.
const char* opName(OpKind k);

} // namespace br
