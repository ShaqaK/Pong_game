from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_the_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with both paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball passes the right paddle
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect if the ball passes the right paddle
    if ball.xcor() < -380:
        ball.reset_position()













screen.exitonclick()









