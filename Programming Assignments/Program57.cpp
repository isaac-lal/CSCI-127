// Name: Isaac Lal
// Email: isaac.lal46@myhunter.cuny.edu
// Date: December 7, 2021
// Programming Assignment #57

#include <iostream>
using namespace std;

int main() {
    int temp;
    cout << "Enter the temperature: ";
    cin >> temp;
    if (temp <= 32) {
        cout << "It's freezing!";
    }
    else if (temp < 68) {
        cout << "It's cold";
    }
    else if (temp < 73){
        cout << "It's warm";
    }
    else if (temp >= 73){
        cout << "It's hot";
    }
}