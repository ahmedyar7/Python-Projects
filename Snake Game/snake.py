# TODO:  control the direction by providin the key binds up down left and right

from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.make_snake_body()
        self.head = self.snake_segments[0]

    def make_snake_body(self):
        ## Making 3 segments
        for position in STARTING_POSITIONS:
            new_segments = Turtle("square")
            new_segments.color("white")
            new_segments.penup()
            new_segments.goto(position)

            self.snake_segments.append(new_segments)

    def move(self):

        for num_seg in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[num_seg - 1].xcor()
            new_y = self.snake_segments[num_seg - 1].ycor()

            self.snake_segments[num_seg].goto(new_x, new_y)

        self.head.forward(MOVEMENT_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
