// Name: Isaac Lal
// Email: isaac.lal46@myhunter.cuny.edu
// Date: December 9, 2021
// Programming Assignment #59

#include <iostream>
using namespace std;

int main() {
    float budget;
    float spending;
    cout << "Enter your monthly budget for food and coffee: ";
    cin >> budget;
    cout << "How much are you spending in a week for coffee: ";
    cin >> spending;
    
    for (int x = 1; x < 5; x++) {
        budget -= spending;
        cout << "Budget left after week " << x << '\t' << budget << '\n';
    }
}