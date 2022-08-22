# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: November 5, 2021
# Programming Assignment #37

import pandas as pd

file = input("Enter file name: ")

df = pd.read_csv(file)

print("There are",df["Name"].size,"total games")
print("The number of games in each genre are")
print(df.Genre.value_counts())
print("The top 3 game publishers are")
print(df.Publisher.value_counts()[:3])