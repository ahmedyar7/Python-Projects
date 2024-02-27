from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(x=0, y=0)
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        self.newX = self.xcor() + self.xMove
        self.newY = self.ycor() + self.yMove
        self.goto(self.newX, self.newY)

    def bounce(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9

    def resetBall(self):
        self.goto(0, 0)
        self.bounceX()
