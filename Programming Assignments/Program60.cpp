// Name: Isaac Lal
// Email: isaac.lal46@myhunter.cuny.edu
// Date: December 10, 2021
// Programming Assignment #60

#include <iostream>
using namespace std;

int main() {
    int num;
    int x;
    int b = 16;
    cout << "Enter a number: ";
    cin >> num;

    if (num < 0) {
        cout << 1;
        x = 32 + num;
    }
    else {
        cout << 0;
        x = num;
    }

    while (b > 0.5) {
        if (x >= b) {
            cout << 1;
        }
        else {
            cout << 0;
        }
        
        x = x % b;
        b = b / 2;
    }
    cout << '\n';
}