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
        self.goto(x=0, y=0)
        self.move_the_ball()


    def move_the_ball(self):
        initial_y = self.ycor() + 10
        initial_x = self. xcor() + 10
        self.goto(initial_x, initial_y)
