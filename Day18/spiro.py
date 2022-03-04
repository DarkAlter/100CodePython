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

direction = [0,90,180,270]
tim.pensize(15) #setting ketebalan
tim.speed("fastest") #setting kecepatan
for _ in range(200):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(direction))