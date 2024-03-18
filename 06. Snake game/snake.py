from turtle import Turtle

class Snake:


    """Classe che rappresenta un serpente."""

    def __init__(self, x, y):
        """
        Inizializza un nuovo serpente.

        :param x: La coordinata x iniziale del serpente.
        :param y: La coordinata y iniziale del serpente.
        """
        self.segments = []
        self.positions = [[x, y], [x - 20, y], [x - 40, y]]
        self.create_snake()
        self.up()
        self.down()
        self.right()
        self.left()

    def create_snake(self):
        """
        Crea un serpente con il colore specificato e posizionato alle coordinate specificate.
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
            self.segments[s].goto(new_x, new_y)

        self.segments[0].forward(10)
        self.positions[0] = [self.segments[0].xcor(), self.segments[0].ycor()]

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

    def extend(self):
        """
        Aggiungo un elemento
        """
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(t)

