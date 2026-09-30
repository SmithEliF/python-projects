from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score = 0
        with open("snake/high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def reset(self):

        self.score = 0


    def point(self):

        self.score += 1

    def update_high_score(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake/high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
