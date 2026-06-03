// player.h -- the player avatar.
//
// Health is one 8-bit register. The player dies when every bit is 0.
// Energy is a separate decimal pool that limits how many weapons can
// be used per turn.

#pragma once
#include <cstdint>
#include <string>

namespace br {

struct Player {
    std::string name;
    uint8_t     health;     // 0b00000000 == dead, 0b11111111 == full HP
    uint8_t     shield;     // reserved for future use / display
    int         energy;     // current spendable energy
    int         maxEnergy;  // cap for regen
    int         score;
    int         kills;

    Player();

    bool alive() const;
    void takeDamage(uint8_t newHealth); // setter; caller computes the masked value
    void heal(uint8_t mask);            // OR-heal: health |= mask
    void regenEnergy(int amount);
    bool spend(int cost);               // returns false if energy insufficient
};

} // namespace br
