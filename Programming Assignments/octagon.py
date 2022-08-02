# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: February 15, 2022
# Programming Assignment #2: Write a program that draws an Octagon.

import turtle

wn = turtle.Screen()
octo = turtle.Turtle()

octo.penup()
octo.setpos(-50, -50)
octo.pendown()

for i in range(8):
    octo.forward(50)
    octo.left(45)