// game.cpp -- orchestrator: menus, campaign loop, combat turns.

#include "game.h"
#include "ui.h"
#include "binary.h"
#include "bitops.h"
#include "level.h"
#include "score.h"
#include "minigame.h"

#include <iostream>
#include <string>

namespace br {

// ----------------------------------------------------------------------
// Construction & arsenal setup
// ----------------------------------------------------------------------

Game::Game() : currentLevel(1), quitRequested(false) {
    setupArsenal();
}

void Game::setupArsenal() {
    arsenal = {
        {"AND Cleaver",  "&",   OpKind::AND,   2, "target = target & mask  (clears bits)"},
        {"OR Mender",    "|",   OpKind::OR,    2, "self   = self   | mask  (heals/shields)"},
        {"XOR Bomb",     "^",   OpKind::XOR,   3, "target = target ^ mask  (toggles bits)"},
        {"NOT Strike",   "~",   OpKind::NOT,   4, "target = ~target        (full invert)"},
        {"Left Shift",   "<<",  OpKind::SHL,   3, "target = target << n    (amplify/lose MSB)"},
        {"Right Shift",  ">>",  OpKind::SHR,   3, "target = target >> n    (halve, deadly)"},
        {"Rotate Left",  "<<<", OpKind::ROTL,  3, "target = rotL(target,n) (wrap-around)"},
        {"Bit Lance",    "=1",  OpKind::SET,   1, "target = target | (1<<n) (set one bit)"},
        {"Bit Snap",     "=0",  OpKind::CLEAR, 1, "target = target & ~(1<<n)(clear one bit)"},
    };
}

// ----------------------------------------------------------------------
// Top-level flow
// ----------------------------------------------------------------------

void Game::run() {
    enableAnsi();
    clearScreen();
    banner();

    std::cout << "\nEnter your hero's name: ";
    std::getline(std::cin, player.name);
    if (player.name.empty()) {
        player.name = "Hero";
    }
    // Strip spaces so the score file format (space-delimited) stays clean.
    for (auto& c : player.name) if (c == ' ') c = '_';

    mainMenu();
}

void Game::mainMenu() {
    while (!quitRequested) {
        std::cout << "\n--- MAIN MENU ---\n";
        std::cout << "1) Start Campaign\n";
        std::cout << "2) Tutorial (Binary & Bitwise basics)\n";
        std::cout << "3) High Scores\n";
        std::cout << "4) Quit\n";
        std::cout << "> ";

        std::string choice;
        std::getline(std::cin, choice);

        if      (choice == "1") startCampaign();
        else if (choice == "2") tutorial();
        else if (choice == "3") printTopScores("scores.txt");
        else if (choice == "4") quitRequested = true;
    }
    std::cout << "\nFarewell, " << player.name << ".\n";
}

void Game::tutorial() {
    std::cout << "\n" << colorCyan("--- TUTORIAL: Binary & Bitwise ---") << "\n";
    std::cout << "Health is an 8-bit value: bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0\n";
    std::cout << "  decimal 170 = binary " << toBinary(170) << "\n";
    std::cout << "  decimal  15 = binary " << toBinary(15)  << "\n";
    std::cout << "  decimal 255 = binary " << toBinary(255) << "\n\n";

    std::cout << "Bitwise operators (worked examples):\n";
    std::cout << "  AND (&) : 1 only where BOTH are 1.\n";
    std::cout << "            " << toBinary(0b11001100) << " & " << toBinary(0b10101010)
              << " = " << toBinary(0b11001100 & 0b10101010) << "\n";
    std::cout << "  OR  (|) : 1 where EITHER is 1.\n";
    std::cout << "            " << toBinary(0b11001100) << " | " << toBinary(0b10101010)
              << " = " << toBinary(0b11001100 | 0b10101010) << "\n";
    std::cout << "  XOR (^) : 1 where bits DIFFER.\n";
    std::cout << "            " << toBinary(0b11001100) << " ^ " << toBinary(0b10101010)
              << " = " << toBinary(0b11001100 ^ 0b10101010) << "\n";
    std::cout << "  NOT (~) : flips every bit.\n";
    std::cout << "            ~" << toBinary(0b00001111)
              << " = " << toBinary(static_cast<uint8_t>(~0b00001111u)) << "\n";
    std::cout << "  SHL (<<): multiply by 2; high bits fall off.\n";
    std::cout << "            " << toBinary(0b00010101) << " << 2 = "
              << toBinary(static_cast<uint8_t>(0b00010101 << 2)) << "\n";
    std::cout << "  SHR (>>): divide by 2; low bits fall off.\n";
    std::cout << "            " << toBinary(0b10100000) << " >> 2 = "
              << toBinary(static_cast<uint8_t>(0b10100000 >> 2)) << "\n\n";

    std::cout << "Tactical tips:\n";
    std::cout << "  - To wipe an enemy: AND with 0 in the bits you want gone.\n";
    std::cout << "  - To heal yourself: OR your HP with a mask of 1s.\n";
    std::cout << "  - To flip a known pattern to its inverse: XOR with the same pattern.\n";
    std::cout << "  - To bypass a shield: chip it down with XOR first.\n";

    pause();
}

// ----------------------------------------------------------------------
// Campaign / level
// ----------------------------------------------------------------------

void Game::startCampaign() {
    player = Player();
    // Preserve the name set earlier in run().
    std::cout << "\nWho draws the bits? Enter your hero's name: ";
    std::getline(std::cin, player.name);
    if (player.name.empty()) player.name = "Hero";
    for (auto& c : player.name) if (c == ' ') c = '_';

    currentLevel = 1;
    std::cout << "\n" << colorYellow("== CAMPAIGN BEGINS ==") << "\n";

    for (int n = 1; n <= totalLevels(); ++n) {
        currentLevel = n;
        playLevel(n);
        if (quitRequested) return;
        if (!player.alive()) {
            gameOverArt();
            recordScore();
            return;
        }
    }
    victoryArt();
    recordScore();
}

void Game::playLevel(int n) {
    Level L = getLevel(n);
    std::cout << "\n"
              << colorCyan("=== LEVEL " + std::to_string(n) + ": " + L.title + " ===")
              << "\n";
    // Modest energy boost between stages.
    player.regenEnergy(4);

    for (auto kind : L.enemies) {
        Enemy e = makeEnemy(kind);
        std::cout << "\nA wild " << e.name << " appears!\n";

        if (!fight(e)) return;          // player died or quit
        if (quitRequested) return;

        player.score += e.rewardScore;
        player.kills++;
        std::cout << colorGreen("Defeated! +") << e.rewardScore << " score.\n";

        // Knights drop a chest -> binary lock-pick minigame.
        if (e.kind == EnemyKind::Knight) {
            std::cout << "\nThe Knight dropped a binary lock chest...\n";
            uint8_t target = static_cast<uint8_t>(e.attackMask | 0b01000010);
            player.score += playLockPick(target);
        }
    }
}

// ----------------------------------------------------------------------
// Combat loop
// ----------------------------------------------------------------------

bool Game::fight(Enemy& enemy) {
    int round = 1;
    while (player.alive() && enemy.alive() && !quitRequested) {
        std::cout << "\n" << colorYellow("--- Round " + std::to_string(round) + " ---") << "\n";
        showStatus(enemy);

        if (!playerTurn(enemy)) continue;     // invalid input -> re-prompt
        if (!enemy.alive()) return true;
        if (quitRequested)  return true;

        enemyTurn(enemy);
        player.regenEnergy(2);
        ++round;
    }
    return player.alive();
}

void Game::showStatus(const Enemy& enemy) {
    std::cout << "\n";
    drawBitBar(player.name + " HP", player.health);
    std::cout << "Energy: " << player.energy << "/" << player.maxEnergy
              << "   Score: " << player.score << "\n\n";

    drawBitBar(enemy.name + "  HP", enemy.health);
    drawBitBar("  Shield ", enemy.shield);
    std::cout << "  Attack mask: " << toBinary(enemy.attackMask) << "\n";
}

void Game::showArsenal() {
    std::cout << "\nArsenal:\n";
    for (size_t i = 0; i < arsenal.size(); ++i) {
        const auto& w = arsenal[i];
        std::cout << "  " << (i + 1) << ") " << w.name
                  << " [" << w.symbol << "]"
                  << "  cost=" << w.energyCost
                  << "  -- " << w.description << "\n";
    }
    std::cout << "  0) skip turn (regen +3 energy)\n";
    std::cout << "  h) help/tutorial\n";
    std::cout << "  q) quit to menu\n";
}

// Convert the user's mask input into a uint8_t.
// Accepts either an 8-character binary string of '0'/'1' or a decimal.
uint8_t Game::readMask(const Weapon& w) {
    if (w.op == OpKind::NOT) return 0;   // NOT ignores the mask

    if (w.op == OpKind::SHL  || w.op == OpKind::SHR  ||
        w.op == OpKind::ROTL || w.op == OpKind::ROTR ||
        w.op == OpKind::SET  || w.op == OpKind::CLEAR) {
        std::cout << "Enter bit count/position (0-7): ";
    } else {
        std::cout << "Enter mask as 8-bit binary (e.g. 11110000) or decimal (0-255): ";
    }

    std::string line;
    std::getline(std::cin, line);
    if (line.empty()) return 0;

    // Pure binary if every char is '0' or '1' and length is 8.
    bool isBinary = (line.size() == 8);
    if (isBinary) {
        for (char c : line) {
            if (c != '0' && c != '1') { isBinary = false; break; }
        }
    }
    if (isBinary) return fromBinary(line);

    try {
        int v = std::stoi(line);
        if (v < 0)   v = 0;
        if (v > 255) v = 255;
        return static_cast<uint8_t>(v);
    } catch (...) {
        return 0;
    }
}

bool Game::playerTurn(Enemy& enemy) {
    showArsenal();
    std::cout << "> ";

    std::string choice;
    std::getline(std::cin, choice);

    if (choice == "q" || choice == "Q") {
        quitRequested = true;
        return true;
    }
    if (choice == "h" || choice == "H") {
        tutorial();
        return false;
    }
    if (choice == "0") {
        player.regenEnergy(3);
        std::cout << "You catch your breath. (+3 energy)\n";
        return true;
    }

    int idx = 0;
    try { idx = std::stoi(choice); }
    catch (...) { return false; }
    if (idx < 1 || idx > static_cast<int>(arsenal.size())) return false;

    const Weapon& w = arsenal[idx - 1];
    if (!player.spend(w.energyCost)) {
        std::cout << colorRed("Not enough energy.") << " (need " << w.energyCost
                  << ", have " << player.energy << ")\n";
        return false;
    }

    uint8_t mask = readMask(w);

    // OR Mender heals the player; everything else targets the enemy.
    if (w.op == OpKind::OR) {
        uint8_t before = player.health;
        player.heal(mask);
        std::cout << "You weave " << toBinary(mask)
                  << " into your essence.\n"
                  << "HP: " << toBinary(before)
                  << " -> " << toBinary(player.health) << "\n";
        return true;
    }

    // Apply the operator, then honour the enemy's shield.
    uint8_t before    = enemy.health;
    uint8_t newHealth = applyWeapon(w, enemy.health, mask);
    // Bits within the shield are immutable: take the new value only
    // where shield == 0, otherwise keep the original.
    newHealth = static_cast<uint8_t>(
        (newHealth & ~enemy.shield) | (enemy.health & enemy.shield)
    );
    enemy.health = newHealth;

    int cleared = countSetBits(static_cast<uint8_t>(before & ~enemy.health));
    std::cout << enemy.name << " HP: " << toBinary(before)
              << " -> " << toBinary(enemy.health)
              << "   (" << opName(w.op)
              << ", cleared " << cleared << " bit" << (cleared == 1 ? "" : "s") << ")\n";

    // XOR also chips at the shield -- thematic and tactically necessary
    // for the Dragon.
    if (w.op == OpKind::XOR) {
        enemy.shield = bAnd(enemy.shield, bNot(mask));
    }
    return true;
}

void Game::enemyTurn(Enemy& enemy) {
    if (!enemy.alive()) return;
    uint8_t before = player.health;
    player.takeDamage(enemyAttack(enemy, player.health));
    std::cout << enemy.name << " attacks with mask " << toBinary(enemy.attackMask)
              << ".\n"
              << "Your HP: " << toBinary(before)
              << " -> " << toBinary(player.health) << "\n";
}

// ----------------------------------------------------------------------
// Persistence
// ----------------------------------------------------------------------

void Game::recordScore() {
    ScoreEntry e{ player.name, player.score, currentLevel };
    saveScore("scores.txt", e);
    std::cout << "\nFinal score: " << player.score
              << "   Kills: "       << player.kills
              << "   Level reached: " << currentLevel << "\n";
    printTopScores("scores.txt");
}

} // namespace br
