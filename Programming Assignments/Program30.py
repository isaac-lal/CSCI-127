# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 27, 2021
# Programming Assignment #30

import pandas as pd

file = input("Enter file name: ")

df = pd.read_csv(file)
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")

style = df.groupby("Style")

print("The average stars per serving style: \nStyle")
print("Bar",'\t',style.get_group("Bar")["Stars"].mean())
print("Bowl",'\t',style.get_group("Bowl")["Stars"].mean())
print("Box",'\t',style.get_group("Box")["Stars"].mean())
print("Can",'\t',style.get_group("Can")["Stars"].mean())
print("Cup",'\t',style.get_group("Cup")["Stars"].mean())
print("Pack",'\t',style.get_group("Pack")["Stars"].mean())
print("Tray",'\t',style.get_group("Tray")["Stars"].mean())
print("Name: Stars, dtype:",df["Stars"].dtype,"\n")

singapore = df[df.Country == "Singapore"]

id = singapore["Stars"].idxmin()

print(singapore["Brand"][id],
      "Has the lowest rating in Singapore with",
      singapore["Stars"][id],"stars.")