from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.0001, stretch_wid=0.0001)
        self.color("white")
        self.goto(0, 280)
        self.valore1 = 0
        self.valore2 = 0
        self.update()

    def update(self):
        self.write(f" {self.valore1} -  {self.valore2}", False)

    def end(self):
        self.color("red")
        self.goto(0, 0)
        self.write("game over", False)

    def increase1(self):
        self.valore1 += 1
        self.clear()
        self.update()

    def increase2(self):
        self.valore2 += 1
        self.clear()
        self.update()