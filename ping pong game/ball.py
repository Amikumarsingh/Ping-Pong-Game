import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.9
        self.speed_multiplier = 1.0


    def move(self):
        """Move the ball to a new position."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def increase_speed(self):
        self.speed_multiplier *= 1.05
    def bounce_y(self):
        """Bounce the ball off the y-axis."""
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        """Bounce the ball off the x-axis and slow it down."""
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        """Reset the ball's position and speed."""
        self.goto(0, 0)
        self.move_speed = 0.9
        self.x_move = random.choice([-2, 2])
        self.y_move = random.choice([-2, 2])

