#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

string decimalToBinary(long long number) {
    if (number == 0) {
        return "0";
    }

    bool isNegative = number < 0;
    unsigned long long value;

    if (isNegative) {
        value = static_cast<unsigned long long>(-(number + 1)) + 1;
    } else {
        value = static_cast<unsigned long long>(number);
    }

    string binary;
    while (value > 0) {
        binary.push_back((value % 2) + '0');
        value /= 2;
    }

    reverse(binary.begin(), binary.end());
    return isNegative ? "-" + binary : binary;
}

int main() {
    long long decimalNumber;

    cout << "Enter a decimal integer: ";
    cin >> decimalNumber;

    cout << "Binary equivalent: " << decimalToBinary(decimalNumber) << endl;

    return 0;
}
