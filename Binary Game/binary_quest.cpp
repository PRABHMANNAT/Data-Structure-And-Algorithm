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

void showDivisionTrail(int number) {
    cout << "Remainder trail:" << endl;

    while (number > 0) {
        cout << number << " % 2 = " << number % 2 << endl;
        number /= 2;
    }

    cout << "Read the remainders from bottom to top." << endl;
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

int difficultyMax(const Player& player) {
    if (player.keys >= 6) {
        return 255;
    }

    if (player.keys >= 3) {
        return 180;
    }

    return 95;
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

ChallengeResult playDecimalToBinaryMission(int maxDecimal) {
    int decimal = randomInt(12, maxDecimal);
    string expected = decimalToBinary(decimal);

    cout << endl;
    cout << "[Gate Mission] Convert decimal to binary" << endl;
    cout << "Decimal number: " << decimal << endl;
    showDivisionTrail(decimal);

    string answer = trimLower(readLine("Binary answer: "));

    ostringstream explanation;
    explanation << decimal << " in binary is " << expected << ".";

    return {answer == expected, explanation.str()};
}

ChallengeResult playBinaryToDecimalMission(int maxDecimal) {
    int decimal = randomInt(10, maxDecimal);
    string binary = decimalToBinary(decimal);

    cout << endl;
    cout << "[Decoder Mission] Convert binary to decimal" << endl;
    cout << "Binary number: " << binary << endl;

    int answer = readInt("Decimal answer: ");

    ostringstream explanation;
    explanation << binary << " equals " << decimal << " in decimal.";

    return {answer == decimal, explanation.str()};
}

ChallengeResult playMissingBitMission(int maxDecimal) {
    int decimal = randomInt(18, maxDecimal);
    string binary = decimalToBinary(decimal);
    int hiddenIndex = randomInt(0, static_cast<int>(binary.size()) - 1);
    char expected = binary[hiddenIndex];

    string damaged = binary;
    damaged[hiddenIndex] = '?';

    cout << endl;
    cout << "[Repair Mission] Find the missing bit" << endl;
    cout << "Decimal source: " << decimal << endl;
    cout << "Damaged binary: " << damaged << endl;

    string answer = trimLower(readLine("Missing bit (0 or 1): "));

    ostringstream explanation;
    explanation << "The full binary form is " << binary << ", so the missing bit is " << expected << ".";

    return {answer.size() == 1 && answer[0] == expected, explanation.str()};
}

ChallengeResult playPowerGateMission() {
    vector<int> candidates = {2, 4, 8, 16, 32, 64, 3, 6, 12, 24, 48, 96};
    int number = candidates[randomInt(0, static_cast<int>(candidates.size()) - 1)];
    bool expected = isPowerOfTwo(number);

    cout << endl;
    cout << "[Power Gate] Is this number a power of 2?" << endl;
    cout << "Number: " << number << " (" << decimalToBinary(number) << " in binary)" << endl;

    string answer = trimLower(readLine("Type yes or no: "));
    bool playerAnswer = answer == "yes" || answer == "y";

    ostringstream explanation;
    explanation << number << " is " << (expected ? "" : "not ")
                << "a power of 2. Answer: " << yesNo(expected) << ".";

    return {playerAnswer == expected, explanation.str()};
}

ChallengeResult playPlaceValueMission(int maxDecimal) {
    int decimal = randomInt(20, maxDecimal);
    string binary = decimalToBinary(decimal);
    int index = randomInt(0, static_cast<int>(binary.size()) - 1);
    int positionFromRight = static_cast<int>(binary.size()) - 1 - index;
    int placeValue = 1;

    for (int i = 0; i < positionFromRight; ++i) {
        placeValue *= 2;
    }

    int expected = (binary[index] == '1') ? placeValue : 0;

    cout << endl;
    cout << "[Place Mission] Find the decimal value of one binary position" << endl;
    cout << "Binary number: " << binary << " (decimal " << decimal << ")" << endl;
    cout << "Position from left: " << index + 1 << " contains bit '" << binary[index] << "'" << endl;

    int answer = readInt("Decimal value of that position: ");

    ostringstream explanation;
    explanation << "That position has place value " << placeValue
                << ", so its contribution is " << expected << ".";

    return {answer == expected, explanation.str()};
}

ChallengeResult playRandomMission(const Player& player) {
    int mission = randomInt(1, 5);
    int maxDecimal = difficultyMax(player);

    if (mission == 1) {
        return playDecimalToBinaryMission(maxDecimal);
    }

    if (mission == 2) {
        return playBinaryToDecimalMission(maxDecimal);
    }

    if (mission == 3) {
        return playMissingBitMission(maxDecimal);
    }

    if (mission == 4) {
        return playPowerGateMission();
    }

    return playPlaceValueMission(maxDecimal);
}

bool playFinalVault() {
    int code = randomInt(100, 255);
    string expected = decimalToBinary(code);

    cout << endl;
    cout << "========== FINAL VAULT ==========" << endl;
    cout << "Vault decimal code: " << code << endl;
    cout << "Convert it to binary to open the vault." << endl;

    string answer = trimLower(readLine("Vault binary code: "));

    if (answer == expected) {
        cout << "Vault opened. Final code was " << expected << "." << endl;
        return true;
    }

    cout << "Vault stayed locked. Correct binary was " << expected << "." << endl;
    return false;
}

void playMainGame() {
    Player player;
    showTitle();

    cout << "Goal: collect " << KEYS_TO_REACH_VAULT << " keys before health reaches 0." << endl;

    while (player.health > 0 && player.keys < KEYS_TO_REACH_VAULT) {
        showStatus(player);
        ChallengeResult result = playRandomMission(player);
        applyResult(player, result);
    }

    showStatus(player);

    if (player.keys >= KEYS_TO_REACH_VAULT) {
        cout << "You reached the final vault." << endl;
        if (playFinalVault()) {
            player.score += 500;
            cout << "Victory score: " << player.score << endl;
        }
    } else {
        cout << "Game over. Practice the conversions and try again." << endl;
    }
}

void practiceMode() {
    cout << endl;
    cout << "Practice Mode" << endl;
    cout << "Enter -1 to return to the menu." << endl;

    while (true) {
        int decimal = readInt("Decimal number: ");

        if (decimal == -1) {
            return;
        }

        if (decimal < 0) {
            cout << "Use non-negative numbers in this practice mode." << endl;
            continue;
        }

        cout << decimal << " -> " << decimalToBinary(decimal) << endl;
    }
}

bool runSelfTests() {
    return decimalToBinary(0) == "0"
        && decimalToBinary(1) == "1"
        && decimalToBinary(8) == "1000"
        && decimalToBinary(50) == "110010"
        && binaryToDecimal("110010") == 50
        && binaryToDecimal("11111111") == 255
        && isBinaryString("10101")
        && !isBinaryString("10201")
        && isPowerOfTwo(64)
        && !isPowerOfTwo(96);
}

int main(int argc, char* argv[]) {
    if (argc > 1 && string(argv[1]) == "--self-test") {
        bool passed = runSelfTests();
        cout << (passed ? "Self-tests passed." : "Self-tests failed.") << endl;
        return passed ? 0 : 1;
    }

    while (true) {
        showTitle();
        cout << "1. Play Binary Quest" << endl;
        cout << "2. Learn the concept" << endl;
        cout << "3. Practice conversion" << endl;
        cout << "4. Exit" << endl;

        int choice = readInt("Choose: ");

        if (choice == 1) {
            playMainGame();
        } else if (choice == 2) {
            showTutorial();
        } else if (choice == 3) {
            practiceMode();
        } else if (choice == 4) {
            cout << "Goodbye." << endl;
            break;
        } else {
            cout << "Choose a menu option from 1 to 4." << endl;
        }
    }

    return 0;
}
