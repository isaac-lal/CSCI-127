# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 4, 2021
# Programming Assignment #14

import turtle

jeff = turtle.Turtle()
jeff.shape("turtle")

hex = input("Please enter a 6-digit Hexadecimal number: ")

jeff.color("#" + hex)

for i in range(4):
    jeff.forward(100)
    jeff.stamp()
    jeff.left(90)

jeff.forward(100)