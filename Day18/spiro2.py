import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def sprirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(randomColor())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim.speed("fastest") #setting kecepatan

sprirograph(5)
screen.exitonclick()