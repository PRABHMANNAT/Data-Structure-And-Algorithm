// weapon.cpp -- dispatch table from OpKind to the bitops primitive.

#include "weapon.h"
#include "bitops.h"

namespace br {

uint8_t applyWeapon(const Weapon& w, uint8_t target, uint8_t mask) {
    switch (w.op) {
        case OpKind::AND:   return bAnd(target, mask);
        case OpKind::OR:    return bOr (target, mask);
        case OpKind::XOR:   return bXor(target, mask);
        case OpKind::NOT:   return bNot(target);
        // For shift/rotate ops the mask is treated as a bit-count (0-7).
        case OpKind::SHL:   return bShl (target, mask & 7);
        case OpKind::SHR:   return bShr (target, mask & 7);
        case OpKind::ROTL:  return bRotL(target, mask & 7);
        case OpKind::ROTR:  return bRotR(target, mask & 7);
        // SET / CLEAR use the mask as a bit position.
        case OpKind::SET:   return setBit  (target, mask & 7);
        case OpKind::CLEAR: return clearBit(target, mask & 7);
    }
    return target;
}

const char* opName(OpKind k) {
    switch (k) {
        case OpKind::AND:   return "AND";
        case OpKind::OR:    return "OR";
        case OpKind::XOR:   return "XOR";
        case OpKind::NOT:   return "NOT";
        case OpKind::SHL:   return "SHL";
        case OpKind::SHR:   return "SHR";
        case OpKind::ROTL:  return "ROTL";
        case OpKind::ROTR:  return "ROTR";
        case OpKind::SET:   return "SET";
        case OpKind::CLEAR: return "CLEAR";
    }
    return "?";
}

} // namespace br
