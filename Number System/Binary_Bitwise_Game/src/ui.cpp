// ui.cpp -- console UI helpers.

#include "ui.h"
#include "binary.h"
#include <iostream>

#ifdef _WIN32
  #ifndef WIN32_LEAN_AND_MEAN
    #define WIN32_LEAN_AND_MEAN
  #endif
  #include <windows.h>
#endif

namespace br {

void enableAnsi() {
#ifdef _WIN32
    // Turn on virtual-terminal processing so \x1b[...m escapes render
    // as actual colors instead of literal text on modern Windows.
    HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD  mode = 0;
    if (h != INVALID_HANDLE_VALUE && GetConsoleMode(h, &mode)) {
        // 0x0004 == ENABLE_VIRTUAL_TERMINAL_PROCESSING
        SetConsoleMode(h, mode | 0x0004);
    }
#endif
}

void clearScreen() {
    // ANSI: clear screen + move cursor to home.
    std::cout << "\x1b[2J\x1b[H";
}

void pause() {
    std::cout << "\nPress ENTER to continue...";
    std::string dummy;
    std::getline(std::cin, dummy);
}

void title(const std::string& s) {
    std::cout << "\n=== " << s << " ===\n";
}

std::string colorRed   (const std::string& s) { return "\x1b[31m" + s + "\x1b[0m"; }
std::string colorGreen (const std::string& s) { return "\x1b[32m" + s + "\x1b[0m"; }
std::string colorYellow(const std::string& s) { return "\x1b[33m" + s + "\x1b[0m"; }
std::string colorCyan  (const std::string& s) { return "\x1b[36m" + s + "\x1b[0m"; }
std::string colorDim   (const std::string& s) { return "\x1b[90m" + s + "\x1b[0m"; }

void drawBitBar(const std::string& label, uint8_t value, bool useColor) {
    // Render the 8 bits, MSB first. Set bits green, clear bits dim.
    const std::string bits = toBinary(value, 8);
    std::string painted;
    for (char c : bits) {
        if (useColor) {
            painted += (c == '1')
                ? "\x1b[1;32m1\x1b[0m"      // bright green
                : "\x1b[90m0\x1b[0m";       // dim gray
        } else {
            painted += c;
        }
    }
    std::cout << label
              << " [" << painted << "]  "
              << "dec=" << static_cast<int>(value)
              << "  bits=" << countSetBits(value) << '\n';
}

void banner() {
    std::cout << colorCyan(
        "##########################################################\n"
        "#                                                        #\n"
        "#       B I T   R E A L M   --  Binary Battle Arena      #\n"
        "#                                                        #\n"
        "#   Forged from binary. Sharpened by bitwise operators.  #\n"
        "##########################################################\n"
    );
}

void victoryArt() {
    std::cout << colorGreen(
        "\n"
        "     V  I  C  T  O  R  Y\n"
        "  ----------------------------\n"
        "  Every bit of the realm bows.\n"
    );
}

void gameOverArt() {
    std::cout << colorRed(
        "\n"
        "     G A M E   O V E R\n"
        "  -----------------------\n"
        "  Your health bits fell to 0.\n"
    );
}

} // namespace br
