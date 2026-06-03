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

int main() {
    cout << "Binary Quest" << endl;
    cout << "A decimal and binary conversion game." << endl;

    return 0;
}
