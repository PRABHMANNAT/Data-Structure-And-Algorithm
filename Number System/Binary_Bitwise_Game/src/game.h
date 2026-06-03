// game.h -- top-level game orchestrator.
//
// `Game` owns the player, the weapon arsenal, and the campaign cursor.
// Public surface is just `run()`; everything else is internal turn-loop
// machinery.

#pragma once
#include "player.h"
#include "enemy.h"
#include "weapon.h"
#include <vector>

namespace br {

class Game {
public:
    Game();
    void run();

private:
    Player              player;
    std::vector<Weapon> arsenal;
    int                 currentLevel;
    bool                quitRequested;

    void setupArsenal();

    // High-level flow.
    void mainMenu();
    void tutorial();
    void startCampaign();
    void playLevel(int n);

    // Combat loop.
    bool fight(Enemy& enemy);
    bool playerTurn(Enemy& enemy);  // returns true on a real turn
    void enemyTurn (Enemy& enemy);

    // UI helpers used during combat.
    void    showStatus  (const Enemy& enemy);
    void    showArsenal ();
    uint8_t readMask    (const Weapon& w);

    void recordScore();
};

} // namespace br
