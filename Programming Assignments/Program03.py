# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: September 17, 2021
# Programming Assignment #3

import turtle
wn = turtle.Screen()           
wn.bgcolor("khaki")

tess = turtle.Turtle()          
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("violet")
alex.pensize(5)

tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)

alex.left(90)
alex.forward(100)
alex.right(30)
alex.forward(100)
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)

wn.exitonclick()