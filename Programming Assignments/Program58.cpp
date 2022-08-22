// Name: Isaac Lal
// Email: isaac.lal46@myhunter.cuny.edu
// Date: December 8, 2021
// Programming Assignment #58

#include <iostream>
using namespace std;

int main() {
    int num;
    string character;
    string sent;
    cout << "Please enter a number: ";
    cin >> num;
    cout << "Please enter a character: ";
    cin >> character;

    for (int x = 0; x < num; x++){
            sent += character;
            cout << sent << '\n';
    }

    for (int x = 0; x < num; x++){
        cout << sent << '\n';
    }
}