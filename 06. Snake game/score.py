from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.0001, stretch_wid=0.0001)
        self.color("white")
        self.goto(0, 280)
        self.valore = 0
        self.update()
       #self.end()

    def update(self):
        self.write(f"score = {self.valore}", False)

    def end(self):
        self.color("red")
        self.goto(0, 0)
        self.write("game over", False)

    def increase(self):
        self.valore += 1
        self.clear()
        self.update()
