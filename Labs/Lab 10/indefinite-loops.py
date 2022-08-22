import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

while (-50 < trey.xcor() < 50) and (-50 < trey.ycor() < 50):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)