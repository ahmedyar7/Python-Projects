from turtle import Turtle


FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super(). __init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, +250)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
    

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)