# Plotting USGS data

#Include turtles and set up screen:
import turtle
screen = turtle.Screen()
# this assures that the size of the screen will match the map image:
screen.setup(946, 502)
#Set coordinates for latitude and longitude:
screen.setworldcoordinates(-180,-90,180,90)
# now set the background to our map image:
screen.bgpic("map3.jpg")


#Create a turtle and set its shape, color,  and lift up the pen:
thea = turtle.Turtle()
thea.shape('circle')
thea.color('red')
thea.penup()

#Plot NYC:
thea.goto(-74,40)
thea.stamp()


#Return to the origin, when done drawing:
thea.home()
