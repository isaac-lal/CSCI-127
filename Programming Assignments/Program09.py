# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: September 27, 2021
# Programming Assignment #9

phrase = input("Enter a phrase: " )
phrase = phrase[::-1]
print("Reversed phrase:", phrase)
phrase = phrase.upper()
words = phrase.split()
last_letters = ''
for i in words:
    last_letters += (i[-1])
print("Last letters of reversed words:", last_letters)