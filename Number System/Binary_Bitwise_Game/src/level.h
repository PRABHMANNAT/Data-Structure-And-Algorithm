// level.h -- campaign progression.
//
// A Level is a title plus a list of enemies the player must defeat
// in order. The Game class queries getLevel(n) and walks that list.

#pragma once
#include "enemy.h"
#include <string>
#include <vector>

namespace br {

struct Level {
    int                    number;
    std::string            title;
    std::vector<EnemyKind> enemies;
};

Level getLevel(int n);
int   totalLevels();

} // namespace br
