# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: September 28, 2021
# Programming Assignment #10

import string

word = input("Enter a word: ")

new_word = ""

for i in word:
    length = len(string.ascii_uppercase)
    index = string.ascii_uppercase.find(i)
    if index + 13 < length:
        new_word += string.ascii_uppercase[index + 13]
    else:
        new_word += string.ascii_uppercase[(index + 13) - length]

print("Your word in code is", new_word)