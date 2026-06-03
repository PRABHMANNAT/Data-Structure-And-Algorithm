// player.cpp -- player state and the few mutators it supports.

#include "player.h"
#include "bitops.h"

namespace br {

Player::Player()
    : name("Hero"),
      health(0xFF),       // start with all 8 bits set
      shield(0x00),
      energy(8),
      maxEnergy(8),
      score(0),
      kills(0) {}

bool Player::alive() const { return health > 0; }

void Player::takeDamage(uint8_t newHealth) {
    health = newHealth;
}

void Player::heal(uint8_t mask) {
    // OR-heal: any bit set in the mask is forced ON in the player's
    // health. This is the inverse of how enemies attack (which AND
    // with ~mask to clear bits).
    health = bOr(health, mask);
}

void Player::regenEnergy(int amount) {
    energy += amount;
    if (energy > maxEnergy) energy = maxEnergy;
}

bool Player::spend(int cost) {
    if (energy < cost) return false;
    energy -= cost;
    return true;
}

} // namespace br
