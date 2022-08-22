# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 22, 2021
# Programming Assignment #27

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('covidCases.csv')

borough = input("Enter borough name: ")
output = input("Enter output name: ")

pop["Fraction"] = pop[borough]/pop["Case Count"]
pop.plot(x= "Date of Interest", y="Fraction")

print("Min:",pop[borough].min())
print("Max:",pop[borough].max())
print("Mean:",pop[borough].mean())
print("Median:",pop[borough].median())
print("Standard Deviation:",pop[borough].std())

fig = plt.gc()
fig.savefig(output)