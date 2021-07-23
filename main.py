from turtle import Turtle, Screen
from blocks import BlockList
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from round import Round

screen = Screen()
screen.tracer(0)

blocks = BlockList()
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
round = Round()

screen.setup(width=840, height=670)
screen.title("Breakout")
screen.bgcolor("black")

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

turtle = Turtle()
turtle.setposition(-420, 275)
turtle.color("blue")
turtle.forward(840)


def is_collided_with(a, b):
    if abs(a.xcor() - b.xcor()) < 32 and abs(a.ycor() - b.ycor()) < 20:
        return True
    else:
        return False


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    for block in blocks.red_blocks:
        if is_collided_with(ball, block):
            block.hideturtle()
            blocks.red_blocks.remove(block)
            scoreboard.point(7)
            ball.bounce_y()

    for block in blocks.orange_blocks:
        if is_collided_with(ball, block):
            block.hideturtle()
            blocks.orange_blocks.remove(block)
            scoreboard.point(5)
            ball.bounce_y()

    for block in blocks.green_blocks:
        if is_collided_with(ball, block):
            block.hideturtle()
            blocks.green_blocks.remove(block)
            scoreboard.point(3)
            ball.bounce_y()

    for block in blocks.yellow_blocks:
        if is_collided_with(ball, block):
            block.hideturtle()
            blocks.yellow_blocks.remove(block)
            scoreboard.point(1)
            ball.bounce_y()

    if abs(ball.xcor() - paddle.xcor()) < 120 and abs(ball.ycor() - paddle.ycor()) < 10:
        ball.bounce_y()

    if ball.is_at_line():
        ball.bounce_x()

    if ball.is_at_top_line():
        ball.bounce_y()

    if ball.is_at_bottom_line():
        round.change_round()
        ball.reset_position()
        paddle.reset_position()

    if round.round > 3:
        round.hideturtle()
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
