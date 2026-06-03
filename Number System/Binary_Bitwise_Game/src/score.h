// score.h -- persistent high-score table backed by a flat text file.

#pragma once
#include <string>
#include <vector>

namespace br {

struct ScoreEntry {
    std::string name;
    int         score;
    int         levelReached;
};

std::vector<ScoreEntry> loadScores(const std::string& path);
void                    saveScore(const std::string& path, const ScoreEntry& e);
void                    printTopScores(const std::string& path, int top = 10);

} // namespace br
