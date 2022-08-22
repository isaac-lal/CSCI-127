# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 28, 2021
# Programming Assignment #31

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of outfile file: ")

df = pd.read_csv(file)

df["Fraction Single Adults"] = df["Total Single Adults in Shelter"] / df["Total Individuals in Shelter"]

df.plot(x = "Date of Census", y = "Fraction Single Adults")

fig = plt.gcf()
fig.savefig(output)