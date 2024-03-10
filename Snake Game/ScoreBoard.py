from turtle import Turtle

ALGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score} ", align=ALGNMENT, font=FONT)
        self.hideturtle()

    def updateScoreBoard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.updateScoreBoard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()
