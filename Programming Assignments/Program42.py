# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: November 12, 2021
# Programming Assignment #42

import folium

map = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.7420577, -74.0101494], popup = "Little Island").add_to(map)

map.save("nycMap.html")