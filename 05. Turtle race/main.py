from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_f():
    my_turtle.forward(20)


def move_b():
    my_turtle.backward(20)


def move_cl():
    my_turtle.left(20)


def move_rt():
    my_turtle.right(20)


screen.listen()
#screen.onkey(key="space",fun=move_f())
screen.onkey(move_f, "Up")
screen.onkey(move_b, "Down")
screen.onkey(move_rt, "Right")
screen.onkey(move_cl, "Left")
screen.exitonclick()