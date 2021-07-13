from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-170, 290)
        self.write(f'Score: {self.score}', align="center", font=("Courier", 30, "normal"))

    def point(self, points):
        self.score += points
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER \nYour score: {self.score} ", align="center", font=("Arial", 40, "normal"))
