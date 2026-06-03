// level.cpp -- the 5 hand-crafted campaign stages.

#include "level.h"

namespace br {

int totalLevels() { return 5; }

Level getLevel(int n) {
    Level L;
    L.number = n;
    switch (n) {
        case 1:
            L.title   = "The Whispering Caves";
            L.enemies = { EnemyKind::Goblin };
            break;
        case 2:
            L.title   = "Iron Bastion";
            L.enemies = { EnemyKind::Goblin, EnemyKind::Knight };
            break;
        case 3:
            L.title   = "Spire of Logic";
            L.enemies = { EnemyKind::Wizard, EnemyKind::Wizard };
            break;
        case 4:
            L.title   = "Hall of Shadows";
            L.enemies = { EnemyKind::Knight, EnemyKind::Phantom };
            break;
        case 5:
            L.title   = "Lair of the Bit Dragon";
            L.enemies = { EnemyKind::Phantom, EnemyKind::Dragon };
            break;
        default:
            L.title = "Unknown Realm";
            break;
    }
    return L;
}

} // namespace br
