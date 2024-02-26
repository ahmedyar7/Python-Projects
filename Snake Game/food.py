from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "blue"
SPEED = "fastest"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.createFood()

    def createFood(self):  ## Constructor Function
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(COLOR)
        self.speed(SPEED)

    def randomFoodLocation(self):  ## Member FUnction
        self.randomX = random.randint(-280, 280)
        self.randomY = random.randint(-280, 280)
        self.goto(self.randomX, self.randomY)
