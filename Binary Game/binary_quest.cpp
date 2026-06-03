#include <algorithm>
#include <chrono>
#include <cctype>
#include <iostream>
#include <limits>
#include <random>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const int STARTING_HEALTH = 5;
const int KEYS_TO_REACH_VAULT = 8;
const int CORRECT_SCORE = 100;
const int STREAK_BONUS = 25;

struct Player {
    int health = STARTING_HEALTH;
    int keys = 0;
    int score = 0;
    int streak = 0;
    int roundsPlayed = 0;
};

struct ChallengeResult {
    bool correct = false;
    string explanation;
};

string trimLower(string text) {
    string result;

    for (char ch : text) {
        if (!isspace(static_cast<unsigned char>(ch))) {
            result.push_back(static_cast<char>(tolower(static_cast<unsigned char>(ch))));
        }
    }

    return result;
}

string readLine(const string& prompt) {
    string input;
    cout << prompt;
    getline(cin, input);
    return input;
}

int readInt(const string& prompt) {
    int value;

    while (true) {
        cout << prompt;

        if (cin >> value) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return value;
        }

        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Please enter a valid whole number." << endl;
    }
}

string decimalToBinary(int number) {
    if (number == 0) {
        return "0";
    }

    string binary;

    while (number > 0) {
        int rem = number % 2;
        binary.push_back(static_cast<char>('0' + rem));
        number /= 2;
    }

    reverse(binary.begin(), binary.end());
    return binary;
}

vector<int> divisionTrail(int number) {
    vector<int> trail;

    while (number > 0) {
        trail.push_back(number % 2);
        number /= 2;
    }

    return trail;
}

bool isBinaryString(const string& text) {
    if (text.empty()) {
        return false;
    }

    for (char ch : text) {
        if (ch != '0' && ch != '1') {
            return false;
        }
    }

    return true;
}

int binaryToDecimal(const string& binary) {
    int answer = 0;
    int pow = 1;

    for (int i = static_cast<int>(binary.size()) - 1; i >= 0; --i) {
        if (binary[i] == '1') {
            answer += pow;
        }

        pow *= 2;
    }

    return answer;
}

bool isPowerOfTwo(int number) {
    if (number <= 0) {
        return false;
    }

    while (number > 1) {
        if (number % 2 != 0) {
            return false;
        }

        number /= 2;
    }

    return true;
}

string yesNo(bool value) {
    return value ? "yes" : "no";
}

void applyResult(Player& player, const ChallengeResult& result) {
    ++player.roundsPlayed;

    if (result.correct) {
        ++player.keys;
        ++player.streak;
        player.score += CORRECT_SCORE + (player.streak - 1) * STREAK_BONUS;
        cout << "Correct. Key collected." << endl;
    } else {
        --player.health;
        player.streak = 0;
        cout << "Wrong. Health lost." << endl;
    }

    cout << result.explanation << endl;
}

void showStatus(const Player& player) {
    cout << endl;
    cout << "Health: " << player.health << "/" << STARTING_HEALTH << " | ";
    cout << "Keys: " << player.keys << "/" << KEYS_TO_REACH_VAULT << " | ";
    cout << "Score: " << player.score << " | ";
    cout << "Streak: " << player.streak << endl;
}

mt19937& rng() {
    static mt19937 engine(static_cast<unsigned int>(
        chrono::steady_clock::now().time_since_epoch().count()
    ));

    return engine;
}

int randomInt(int low, int high) {
    uniform_int_distribution<int> dist(low, high);
    return dist(rng());
}

void showTitle() {
    cout << endl;
    cout << "======================================" << endl;
    cout << "          BINARY QUEST" << endl;
    cout << "======================================" << endl;
    cout << "Convert, decode, repair, and unlock." << endl;
}

void showTutorial() {
    cout << endl;
    cout << "Core idea:" << endl;
    cout << "Decimal to binary repeatedly divides by 2." << endl;
    cout << "% 2 gives the next binary digit." << endl;
    cout << "/ 2 moves the number to the next step." << endl;
    cout << endl;
    cout << "Example for 50:" << endl;
    cout << "50 % 2 = 0" << endl;
    cout << "25 % 2 = 1" << endl;
    cout << "12 % 2 = 0" << endl;
    cout << " 6 % 2 = 0" << endl;
    cout << " 3 % 2 = 1" << endl;
    cout << " 1 % 2 = 1" << endl;
    cout << "Bottom to top: 110010" << endl;
    cout << endl;
}

int main() {
    cout << "Binary Quest" << endl;
    cout << "A decimal and binary conversion game." << endl;

    return 0;
}
