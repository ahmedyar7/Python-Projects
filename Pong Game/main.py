from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()

# SETTING UP THE SCREEN:
screen.bgcolor("black")
screen.title("PONG")
screen.setup(height=600, width=800)
screen.tracer(0)


# OBJECTS:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


# RESPONSE TO THE UP AND DOWN FUNCTIONS FOR BOTH THE PADDLE CREATED:
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


# UPDATE SCREEN MANUALLY BY USING WHILE LOOP
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with the wall when ball hit any 300px in the screen:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with right paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # detect when right paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        # detect when left paddle missies
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
