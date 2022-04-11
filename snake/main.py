import time
from turtle import Turtle, Screen
from snake import snake

screen = Screen()
screen.setup(height=600, width = 600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
snake = snake()
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")


gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()