from turtle import Turtle


# Created the class the inherit from the turtle class:
class Paddle(Turtle):
    # Initialize the attributes for the paddle class
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)  # Position arg is passed form l_paddle and r_paddle

        # defining the moving up and down key

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
