from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.reset()
        self.sety(280)
        self.hideturtle()
        self.pencolor("white")
        self.write(f"score is: {self.score}", move=False, align="center")

    def increase_score(self):
        self.score += 1
        self.reset()
        self.sety(280)
        self.hideturtle()
        self.pencolor("white")
        self.write(f"score is: {self.score}", move=False, align="center")

    def gameover(self):
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.sety(0)
        self.write(f"GAME OVER.", move=False, align="center")