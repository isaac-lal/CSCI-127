# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 6, 2021
# Programming Assignment #16

choice = input("enter 'a' for Light-Year to Parsec,\nenter 'b' for Parsec to Light-Year.\n")

print("Your selection:",choice)

if choice == 'a':
    x = input("Please enter a number of Light-Years: ")
    converted = float(x)/3.26156378
    print(float(x),"Light-Years is equal to",converted,"Parsecs.")
else:
    x = input("Please enter a number of Parsecs: ")
    converted = float(x)*3.26156378
    print(float(x),"Parsecs is equal to",converted,"Light-Years.")