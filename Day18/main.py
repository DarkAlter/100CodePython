import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
def tagon(sides):
    for a in range(sides):
        angle = 360/sides
        tim.color(randomColor())
        tim.forward(100)
        tim.right(angle)
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
for b in range(3,11):
    tagon(b)
screen.exitonclick()