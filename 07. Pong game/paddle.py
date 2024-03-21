from turtle import Turtle


class Paddle:

    def __init__(self, x, y):
        """
        Inizializza la paletta dell'utente.

        :param x: La coordinata x iniziale del paddle.
        :param y: La coordinata y iniziale del paddle.
        """
        self.segments = []
        self.positions = [[x, y], [x, y-20], [x, y-40], [x, y-60], [x, y-80]]
        self.create_paddle()
        self.up()
        self.down()


    def create_paddle(self):
        """
        Crea la paddle con il colore specificato e posizionato alle coordinate specificate.
        """
        for position in self.positions:
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(position[0], position[1])
            self.segments.append(t)

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1): # così lo zero viene lasciato fuori
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y-10)
        self.positions[0] = [self.segments[0].xcor(), self.segments[0].ycor()]

    def up(self):
        self.segments[0].setheading(90)
        self.segments[0].forward(50)

    def down(self):
        self.segments[0].setheading(270)
        self.segments[0].forward(50)