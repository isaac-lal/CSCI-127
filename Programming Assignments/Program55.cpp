// Name: Isaac Lal
// Email: isaac.lal46@myhunter.cuny.edu
// Date: December 3, 2021
// Programming Assignment #55

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float amount;
    cout << "Enter amount in cryptocurrency: ";
    cin >> amount;
    cout << fixed << setprecision(2);
    cout << amount << " BTC in USD: $" << amount * 31901.19 << '\n';
    cout << amount << " ETH in USD: $" << amount * 1901.54 << '\n';
    cout << amount << " DOGE in USD: $" << amount * 0.179733;
}