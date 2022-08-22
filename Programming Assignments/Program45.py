# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: November 17, 2021
# Programming Assignment #45

import pandas as pd
import folium

file = input("Please enter the name of the input file: ")
output = input("Please enter the name of the output file: ")
borough = input("Please enter the name of the borough: ")

df = pd.read_csv(file)

data = df.groupby("City").get_group(borough)


map = folium.Map(location=[40.768731, -73.964915],zoom_start=10)

for index,row in data.iterrows():
    lat = data['Latitude'][index]
    lon = data['Longitude'][index]
    name = data["Location"][index]
    newMarker = folium.Marker([lat,lon], popup=name)
    newMarker.add_to(map)

map.save(output)