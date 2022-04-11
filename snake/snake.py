from turtle import Turtle
START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class snake:
    def __init__(self):
        self.segments = []
        self.createSnakes()
        self.heads = self.segments[0]

    def createSnakes(self):
        for position in START:
            newSegments = Turtle("square")
            newSegments.color("white")
            newSegments.penup()
            newSegments.goto(position)
            self.segments.append(newSegments)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.heads.forward(MOVE_DISTANCE)
    def up(self):
        self.heads.setheading(90)

    def down(self):
        self.heads.setheading(270)

    def left(self):
        self.heads.setheading(180)

    def right(self):
        self.heads.setheading(0)
