// minigame.cpp -- the lock-pick implementation.

#include "minigame.h"
#include "binary.h"
#include "bitops.h"
#include "ui.h"
#include <iostream>
#include <string>

namespace br {

int playLockPick(uint8_t target) {
    std::cout << "\n" << colorYellow("-- BINARY LOCK PICK --") << "\n";
    std::cout << "Current state: " << toBinary(0) << "\n";
    std::cout << "Target state : " << toBinary(target) << "\n";
    std::cout << "Toggle bit positions to match the target.\n";
    std::cout << "Enter positions 0-7 separated by spaces (or 'q' to abandon):\n> ";

    std::string line;
    std::getline(std::cin, line);
    if (line.empty() || line[0] == 'q' || line[0] == 'Q') return 0;

    uint8_t current = 0;
    int     toggles = 0;
    for (char c : line) {
        if (c >= '0' && c <= '7') {
            current = toggleBit(current, c - '0');
            ++toggles;
        }
    }

    std::cout << "Result       : " << toBinary(current) << "\n";

    if (current == target) {
        const int optimal = countSetBits(target);
        const int perfect = (toggles == optimal) ? 50 : 0;
        const int reward  = 50 + perfect;
        std::cout << colorGreen("LOCK OPENED!")
                  << " +" << reward << " score"
                  << (perfect ? " (PERFECT)" : "")
                  << "\n";
        return reward;
    }
    std::cout << colorRed("Wrong pattern.") << " No bonus.\n";
    return 0;
}

} // namespace br
