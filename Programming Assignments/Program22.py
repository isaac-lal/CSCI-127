# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 15, 2021
# Programming Assignment #22

import turtle				

turtle.colormode(255) #Allows colors to be given as 0...255

jeff = turtle.Turtle()

jeff.speed(0)
jeff.pensize(5)

wn = turtle.Screen()
wn.bgcolor("khaki")

for i in range(36):
    jeff.pencolor(0,i*7,0)
    jeff.forward(10)
    jeff.left(10)
    for j in range(4):
        jeff.left(90)
        jeff.forward(300)
        jeff.backward(50)