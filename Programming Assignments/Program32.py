# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 29, 2021
# Programming Assignment #32

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of outfile file: ")

df = pd.read_csv(file)

groupedData = df.groupby("state")
averageStates = groupedData["duration (seconds)"].mean()
topTen = averageStates.sort_values(ascending=False)[:10]
print(topTen.head())

topTen.plot.bar("state","seconds")
plt.xlabel("State")
plt.ylabel("Seconds")

fig = plt.gcf()
fig.savefig(output)