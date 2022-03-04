import turtle
from turtle import Turtle, Screen
import random
isRaceOn = False
screen = Screen()
screen.setup(height=400, width=500)
userbet = screen.textinput(title="make your bet", prompt="which turtle will win?")
colors = ["red","orange","yellow", "green", "blue", "purple"]
y_position = [-70,-40, -10, 20, 50, 80]
allTurtles = []


for turtle_index in range (0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x = -230, y=y_position[turtle_index])
    allTurtles.append(tim)


if userbet:
    isRaceOn = True

while isRaceOn:
    if turtle.xcor() > 230:
        isRaceOn = False
        winningColor = turtle.pencolor()
        if winningColor == userbet:
            print("You Win")
        else:
            print("You Lose")
    for turtle in allTurtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)





screen.exitonclick()