from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.listen()

screen.setup(width=600, height=600)
screen.bgcolor("Black")
is_game_on = True

##  MAKING OBJECT FROM USER DEFINED CLASSES
snake = Snake()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.mainloop()
