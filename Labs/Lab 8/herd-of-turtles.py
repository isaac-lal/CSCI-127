#Intro Programming Lab:  A program with herd of turtles

import turtle


def welcomeMessage():
    print()
    print("Welcome to our herd of turtles demonstration!")
    print()

def getInput():
    n = eval(input("Please enter the number of turtles: "))
    return n


def setUpScreen():
    w = turtle.Screen()
    w.bgcolor("green")
    return w

def setUpTurtles(n):
    tList = []
    #Create turtles:
    for i in range(n):
        t = turtle.Turtle()
        t.shape("turtle")       #Make the turtle appear turtle-shaped
        tList.append(t)

    #Change their color from the blue default and default direction
    for i in range(n):
        tList[i].color(0,0,i/(2*n)+.5)
        tList[i].right(i*360/n)

    return tList

def moveForward(tList):
    for t in tList:
        t.forward(30)

def stamp(tList):
    for t in tList:
        t.stamp()

def main():
    welcomeMessage()            #Writes a welcome message to the shell
    numTurtles = getInput()     #Ask for number of turles
    w = setUpScreen()           #Set up a green turtle window
    turtleList = setUpTurtles(numTurtles) #Make a list of turtles, different colors
    for i in range(10):
        moveForward(turtleList) #Move each turtle in the list forward
        stamp(turtleList)       #Stamp where the turtle stopped


if __name__ == "__main__":
    main()