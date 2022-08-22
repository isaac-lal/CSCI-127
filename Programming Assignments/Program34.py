# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: November 2, 2021
# Programming Assignment #34

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of outfile file: ")

df = pd.read_csv(file)

df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Points"] = 100 * df["Winner Pts"] / (df["Winner Pts"] + df["Loser Pts"])

df.plot(x = "Date", y = "% Points")

fig = plt.gcf()
fig.savefig(output)