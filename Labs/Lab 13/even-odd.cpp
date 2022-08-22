//Name:  CSci 127 Teaching Staff
//Date:  November 2017
//A program demonstrating if-else statements in C++
#include <iostream>
using namespace std;

int main()
{
  int num;
  cout << "Hello!" << endl;
  cout << "Enter a number: ";
  cin >> num;
  if (num % 2 == 0)
  {
    cout << "Even number!\n";
  }
  else
  {
    cout << "Odd number\n";
  }
  return 0;
}
