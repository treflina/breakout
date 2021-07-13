from turtle import Turtle

LEFT_LINE_X = -415
RIGHT_LINE_X = 415


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
        self.setposition(0, -290)

    def move(self):
        new_x = self.xcor() + self.x_move - 1
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -290)
        self.bounce_x()

    def is_at_line(self):
        if self.xcor() < LEFT_LINE_X or self.xcor() > RIGHT_LINE_X:
            return True
        else:
            return False

    def is_at_top_line(self):
        if self.ycor() > 275:
            return True
        else:
            return False

    def is_at_bottom_line(self):
        if self.ycor() < -325:
            return True
        else:
            return False
