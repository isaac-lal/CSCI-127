# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: September 23, 2021
# Programming Assignment #7

message = input("Enter a message: ")

for i in message:
    y = ord(i)
    print(i,"shifted by 5 characters is:", chr(y+5))