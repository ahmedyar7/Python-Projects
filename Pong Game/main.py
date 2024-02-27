from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

## MAKING OBJECT FROM USER DEFINED CLASSES
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreBoard = ScoreBoard()


## Making the Keybinding
screen.onkey(fun=paddle1.moveUp, key="Up")
screen.onkey(fun=paddle1.moveDown, key="Down")

screen.onkey(fun=paddle2.moveUp, key="w")
screen.onkey(fun=paddle2.moveDown, key="s")

gameIsOn = True

while gameIsOn:
    time.sleep(ball.moveSpeed())
    screen.update()
    ball.move()

    if (
        ball.distance(paddle1) < 50
        and ball.xcor() > 320
        or ball.distance(paddle2) < 50
        and ball.xcor() < -320
    ):
        ball.bounceX()

    if ball.xcor() > 380:
        ball.resetBall()
        scoreBoard.leftPoint()

    if ball.xcor() < -380:
        ball.resetBall()
        scoreBoard.rightPoint()


screen.mainloop()
