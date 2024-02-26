from turtle import Turtle

ALGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score} ", align=ALGNMENT, font=FONT)
        self.hideturtle()

    def updateScoreBoard(self):
        self.write(f"Score: {self.score} ", align=ALGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()
