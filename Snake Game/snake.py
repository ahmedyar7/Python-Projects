from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.make_snake_body()
        self.head = self.snake_segments[0]

    def make_snake_body(self):
        ## Making 3 segments
        for position in STARTING_POSITIONS:
            self.addSegment(position)

    ## MOVEMENT IN SNAKE
    def move(self):

        for num_seg in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[num_seg - 1].xcor()
            new_y = self.snake_segments[num_seg - 1].ycor()

            self.snake_segments[num_seg].goto(new_x, new_y)

        self.head.forward(MOVEMENT_DISTANCE)

    ## MOVEMENTS CONTROL IN THE SNAKE

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    ## EXTENSION IN THE SNAKE

    def addSegment(self, position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.snake_segments.append(new_segments)

    def extendSnake(self):
        self.addSegment(self.snake_segments[-1].position())

    ## GAME OVER SEQUENCE
    def collisonWithWall(self):
        if (
            self.head.xcor() > 280
            or self.head.xcor() < -280
            or self.head.ycor() > 280
            or self.head.ycor() < -280
        ):
            return True
        else:
            return False

    def collisionWithTail(self):
        for segments in self.snake_segments[1:]:
            if self.head.distance(segments) < 10:
                return True
            else:
                return False
