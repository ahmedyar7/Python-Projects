import turtle as t
from turtle import Screen
import random

turtle = t.Turtle()
screen = Screen()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


radius = 10
for i in range(1001):
    turtle.speed("fastest")
    radius += 2.5
    turtle.circle(radius)
    turtle.left(2.5)
    turtle.color(random_color())


screen.mainloop()
