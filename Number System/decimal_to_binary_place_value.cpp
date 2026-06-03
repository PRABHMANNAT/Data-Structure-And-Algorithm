#include <iostream>

using namespace std;

/*
    Decimal to binary conversion using the place-value method.

    Example: decNum = 50

    50 % 2 = 0
    25 % 2 = 1
    12 % 2 = 0
     6 % 2 = 0
     3 % 2 = 1
     1 % 2 = 1

    Reading the remainders from bottom to top gives 110010.

    In this method:
    - rem gives the next binary digit.
    - decNum / 2 moves to the next step.
    - pow stores the position: 1, 10, 100, 1000, ...
    - ans builds the final binary-looking number.
*/
long long decToBinary(int decNum) {
    if (decNum == 0) {
        return 0;
    }

    long long ans = 0;
    long long pow = 1;

    while (decNum > 0) {
        int rem = decNum % 2;
        decNum /= 2;

        ans += rem * pow;
        pow *= 10;
    }

    return ans;
}

int main() {
    int decNum;

    cout << "Enter a non-negative decimal number: ";
    cin >> decNum;

    if (decNum < 0) {
        cout << "This method is for non-negative decimal numbers only." << endl;
        return 0;
    }

    cout << "Binary equivalent: " << decToBinary(decNum) << endl;

    return 0;
}
