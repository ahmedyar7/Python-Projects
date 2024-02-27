from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):

        super().__inti__()
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.shape("square")
        self.penup()
        self.goto(position)

        ## PADDLE MOVEMENT

    def moveUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def moveDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)
