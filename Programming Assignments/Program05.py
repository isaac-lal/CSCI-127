# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: September 21, 2021
# Programming Assignment #5

import turtle

wn = turtle.Screen()
wn.bgcolor("khaki")

jeff = turtle.Turtle()
jeff.shape("turtle")
jeff.fillcolor("green")
jeff.pensize(3)

for i in range(6):
    jeff.forward(100)
    jeff.left(45)
    jeff.forward(100)
    jeff.left(135)
    jeff.stamp()
    jeff.forward(100)
    jeff.left(45)
    jeff.forward(100)
    jeff.left(75)