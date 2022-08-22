// Name: Isaac Lal
// Email: isaac.lal46@myhunter.cuny.edu
// Date: December 7, 2021
// Programming Assignment #56

#include <iostream>
using namespace std;

int main() {
    int num;
    string word;
    cout << "Please enter a number: ";
    cin >> num;
    cout << "Please type a word: ";
    cin >> word;
    while (num > 0) {
        cout << num << ',' << '\n';
        num--;
    }
    cout << "Time for " << word << '!';
}