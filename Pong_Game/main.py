from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((365, 0))
left_paddle = Paddle((-365, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# Detecting collision of ball with wall
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()

# Detecting collision with paddle
    if ball.distance(right_paddle)<50 and ball.xcor()>325 or ball.distance(left_paddle)<50 and ball.xcor()<-325:
        ball.bounce_x()

# Counting right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.left_point()

# Counting left paddle misses:
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
