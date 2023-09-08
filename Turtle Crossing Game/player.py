from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super(). __init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.goto_start()
        self.setheading(90)
        self.move_up()
        self.is_at_finish_line()


    def move_up(self):
        self.forward(10)


    def goto_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
       if self.ycor() > FINISH_LINE_Y:
           return True
       else:
           return False


    