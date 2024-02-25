from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


## MOVEMENT FUNCTION:
def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_left():
    turtle.left(100)


def move_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
## KEYBINDS OF THE MOVEMENT
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear_screen)


screen.mainloop()
