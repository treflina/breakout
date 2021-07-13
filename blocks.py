from turtle import Turtle, Screen

screen = Screen()
y_list = [-70, -50, -30, -10, 10, 30, 50, 70]


class BlockList:

    def __init__(self):

        self.red_blocks = []
        self.orange_blocks = []
        self.green_blocks = []
        self.yellow_blocks = []
        self.create_red_blocks()
        self.create_orange_blocks()
        self.create_green_blocks()
        self.create_yellow_blocks()

    def create_red_blocks(self):
        screen.tracer(0)
        for y in y_list[-2:]:
            for i in range(14):
                red = Turtle()
                red.penup()
                red.shape("square")
                red.shapesize(0.9, 2.9)
                red.color("red")
                i = i * 60 - 390
                red.goto(i, y)
                self.red_blocks.append(red)
        screen.update()

    def create_orange_blocks(self):
        screen.tracer(0)
        for y in y_list[4:6]:
            for i in range(14):
                orange = Turtle()
                orange.penup()
                orange.shape("square")
                orange.shapesize(0.9, 2.9)
                orange.color("orange")
                i = i * 60 - 390
                orange.goto(i, y)
                self.orange_blocks.append(orange)
        screen.update()

    def create_green_blocks(self):
        screen.tracer(0)
        for y in y_list[2:4]:
            for i in range(14):
                green = Turtle()
                green.penup()
                green.shape("square")
                green.shapesize(0.9, 2.9)
                green.color("green")
                i = i * 60 - 390
                green.goto(i, y)
                self.green_blocks.append(green)
        screen.update()

    def create_yellow_blocks(self):
        screen.tracer(0)
        for y in y_list[0:2]:
            for i in range(14):
                yellow = Turtle()
                yellow.penup()
                yellow.shape("square")
                yellow.shapesize(0.9, 2.9)
                yellow.color("yellow")
                i = i * 60 - 390
                yellow.goto(i, y)
                self.yellow_blocks.append(yellow)
            screen.update()
