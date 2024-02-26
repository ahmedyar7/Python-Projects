from turtle import Screen
from snake import Snake
from food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.listen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("Black")


##  MAKING OBJECT FROM USER DEFINED CLASSES
snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.randomFoodLocation()
        snake.extendSnake()
        scoreBoard.increaseScore()

    if snake.collisonWithWall():
        is_game_on = False
        scoreBoard.gameOver()

    if snake.collisionWithTail():
        is_game_on = False
        scoreBoard.gameOver()


screen.mainloop()
