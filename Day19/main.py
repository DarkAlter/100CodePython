from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(30)
def back():
    tim.backward(30)
def muterSearahJarumJam():
    tim.left(20)

def counterClockwise():
    tim.right(20)
def clearScreen():
    tim.reset()
screen.listen()
screen.onkey(move_forward,"w")#maju
screen.onkey(back,"s")#mundur
screen.onkey(muterSearahJarumJam,"a")
screen.onkey(counterClockwise,"d")
screen.onkey(clearScreen,"c")
screen.exitonclick()