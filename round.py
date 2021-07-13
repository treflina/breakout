from turtle import Turtle


class Round(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.round = 1
        self.update_round()

    def update_round(self):
        self.clear()
        self.goto(175, 290)
        self.write(f'Round: {self.round}/3', align="center", font=("Arial", 30, "normal"))

    def change_round(self):
        self.round += 1
        self.update_round()
