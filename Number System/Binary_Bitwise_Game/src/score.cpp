// score.cpp -- read/write the on-disk score table.
//
// Storage format is one entry per line:    <name> <score> <levelReached>
// Names with spaces are not supported on purpose -- keeps parsing
// trivial. The Game class strips spaces from the hero name on input.

#include "score.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>

namespace br {

std::vector<ScoreEntry> loadScores(const std::string& path) {
    std::vector<ScoreEntry> out;
    std::ifstream in(path);
    if (!in) return out;

    std::string line;
    while (std::getline(in, line)) {
        std::istringstream iss(line);
        ScoreEntry e;
        if (iss >> e.name >> e.score >> e.levelReached) {
            out.push_back(e);
        }
    }
    return out;
}

void saveScore(const std::string& path, const ScoreEntry& e) {
    std::ofstream out(path, std::ios::app);
    if (!out) return;
    out << e.name << ' ' << e.score << ' ' << e.levelReached << '\n';
}

void printTopScores(const std::string& path, int top) {
    auto v = loadScores(path);
    std::sort(v.begin(), v.end(),
              [](const ScoreEntry& a, const ScoreEntry& b) {
                  return a.score > b.score;
              });

    std::cout << "\n=== HIGH SCORES ===\n";
    if (v.empty()) {
        std::cout << "(no scores yet -- be the first!)\n";
    } else {
        for (size_t i = 0; i < v.size() && static_cast<int>(i) < top; ++i) {
            std::cout << (i + 1) << ". " << v[i].name
                      << "  " << v[i].score << " pts"
                      << "  (Lvl " << v[i].levelReached << ")\n";
        }
    }
    std::cout << "===================\n";
}

} // namespace br
