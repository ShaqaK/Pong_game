from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')



game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
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
        # add one score to left player
        scoreboard.add_score_l()

    # Detect if the ball passes the right paddle
    if ball.xcor() < -380:
        ball.reset_position()
        #add one score to right player
        scoreboard.add_score_r()













screen.exitonclick()









