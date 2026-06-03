// enemy.cpp -- enemy factory and attack resolution.

#include "enemy.h"
#include "bitops.h"

namespace br {

Enemy makeEnemy(EnemyKind k) {
    Enemy e{};
    e.kind = k;
    switch (k) {
        case EnemyKind::Goblin:
            e.name        = "Goblin";
            e.health      = 0b00001111;  // only low nibble lit
            e.shield      = 0b00000000;
            e.attackMask  = 0b00000001;  // chips one bit per turn
            e.rewardScore = 50;
            break;
        case EnemyKind::Knight:
            e.name        = "Knight";
            e.health      = 0b11110000;
            e.shield      = 0b10000000;  // top bit is armoured
            e.attackMask  = 0b00010000;
            e.rewardScore = 120;
            break;
        case EnemyKind::Wizard:
            e.name        = "Wizard";
            e.health      = 0b10101010;  // checkerboard
            e.shield      = 0b00000010;
            e.attackMask  = 0b00001000;
            e.rewardScore = 180;
            break;
        case EnemyKind::Phantom:
            e.name        = "Phantom";
            e.health      = 0b01010101;
            e.shield      = 0b00010000;
            e.attackMask  = 0b00010101;  // strips multiple bits
            e.rewardScore = 220;
            break;
        case EnemyKind::Dragon:
            e.name        = "Dragon";
            e.health      = 0b11111111;  // full HP
            e.shield      = 0b11000011;  // heavy armour on both ends
            e.attackMask  = 0b00111100;
            e.rewardScore = 500;
            break;
    }
    return e;
}

uint8_t enemyAttack(const Enemy& e, uint8_t playerHealth) {
    // "Clear those bits": AND the player's health with the complement
    // of the attack mask. Wherever the mask has a 1, the player loses
    // that bit; everywhere else the player is untouched.
    return bAnd(playerHealth, bNot(e.attackMask));
}

} // namespace br
