from colorList import color_pallet
from turtle import Turtle, Screen, colormode
import random

colormode(255)

turtle = Turtle()
screen = Screen()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

num_of_dots = 100

for dot_counts in range(1, num_of_dots + 1):
    turtle.dot(20, random.choice(color_pallet))
    turtle.forward(50)

    if dot_counts % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen.mainloop()
