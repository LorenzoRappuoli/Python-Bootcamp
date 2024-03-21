from turtle import Turtle


class Ball:

    def __init__(self):
        self.palla = []
        self.create_ball()

    def create_ball (self):

        b = Turtle()
        b.penup()
        b.color("white")
        b.goto(0, 0)
        b.shape("circle")
        self.palla.append(b)
        self.palla[0].setheading(180)

    def move_ball(self):

        self.palla[0].forward(3)