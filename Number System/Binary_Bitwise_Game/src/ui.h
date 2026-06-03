// ui.h -- terminal UI helpers (banner, colored output, bit-bar render).

#pragma once
#include <string>
#include <cstdint>

namespace br {

// On Windows 10+ we must opt in to ANSI escape processing.
void enableAnsi();

void clearScreen();
void pause();
void title(const std::string& s);

// ANSI color wrappers. If the terminal does not support ANSI the
// escapes degrade harmlessly to extra characters (we keep them on by
// default; modern terminals handle them fine).
std::string colorRed   (const std::string& s);
std::string colorGreen (const std::string& s);
std::string colorYellow(const std::string& s);
std::string colorCyan  (const std::string& s);
std::string colorDim   (const std::string& s);

// Render an 8-bit value as a bit-bar: each 1-bit is highlighted, each
// 0-bit dimmed. Followed by decimal + popcount.
void drawBitBar(const std::string& label, uint8_t value, bool useColor = true);

void banner();
void victoryArt();
void gameOverArt();

} // namespace br
