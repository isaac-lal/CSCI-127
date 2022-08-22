# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 1, 2021
# Programming Assignment #13

books = input("Enter a list of book and theirs authors: ")

books_split = books.split(";")

for i in range(len(books_split)):
    books_split[i] = books_split[i].split("-")

for i in range(len(books_split)):
    books_split[i][1] = books_split[i][1].split()[0][0] + "." + books_split[i][1].split()[1][0]

for i in books_split:
    print(i[0].lstrip() + "by " + i[1] + ".")

print("\nThank you for using my book organizer!")