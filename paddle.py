from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=12)
        self.penup()
        self.goto(0, -305)

    def go_left(self):
        new_xcor = self.xcor() - 80
        self.goto(new_xcor, self.ycor())

    def go_right(self):
        new_xcor = self.xcor() + 80
        self.goto(new_xcor, self.ycor())

    def reset_position(self):
        self.goto(0, -305)
