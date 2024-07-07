from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Ball collision with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball collision with the both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball beyond right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Ball beyond left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Increase ball speed every 10 iterations
    if ball.xcor() % 10 == 0:
        ball.increase_speed()

screen.exitonclick()