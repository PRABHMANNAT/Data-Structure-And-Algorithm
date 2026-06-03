// enemy.h -- enemy roster.
//
// Each enemy is mostly data: a starting health pattern, a shield
// (bits the player cannot directly modify), and an attack mask that
// clears that many bits from the player each round.

#pragma once
#include <cstdint>
#include <string>

namespace br {

enum class EnemyKind {
    Goblin,    // weak, sparse bits
    Knight,    // armoured, high nibble set
    Wizard,    // alternating pattern, small shield
    Phantom,   // tricky, attack mask overlaps with shield
    Dragon     // boss, full HP + heavy shield
};

struct Enemy {
    std::string name;
    EnemyKind   kind;
    uint8_t     health;
    uint8_t     shield;        // bits in `shield` are immutable to the player
    uint8_t     attackMask;    // bits this enemy strips from the player each turn
    int         rewardScore;

    bool alive() const { return health > 0; }
};

// Factory: produces a fresh enemy from a kind.
Enemy makeEnemy(EnemyKind k);

// Compute the player's new health after `e` attacks.
// Implemented as playerHealth & ~attackMask -- a textbook "clear bits"
// operation.
uint8_t enemyAttack(const Enemy& e, uint8_t playerHealth);

} // namespace br
