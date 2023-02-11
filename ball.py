from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        #self.goto(x=0, y=0)
        #self.move_the_ball()
        self.x_move = 10
        self.y_move = 10


    def move_the_ball(self):
        initial_y = self.ycor() + self.y_move
        initial_x = self. xcor() + self.x_move

        self.goto(initial_x, initial_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

