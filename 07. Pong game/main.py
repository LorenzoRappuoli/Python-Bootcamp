from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def rimb(l, p):

    for i in l:

        if p.distance(i) <= 15:
            p.setheading(angle + 150 - 15*l.index(i))
            break

    return



# schermo e movimenti

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# inizializzo la paddle del giocatore e del pc

pad1 = Paddle(-500, 0 )
pad2 = Paddle(500, 0 )
ball0 = Ball()
scoreb = Scoreboard()

# rendo lo schermo sensibile ai movimenti


screen.listen()

screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
screen.onkey(pad2.up, "Left")
screen.onkey(pad2.down, "Right")

games_on = True

while games_on:
    screen.update()
    time.sleep(0.01)

    pad1.move()
    pad2.move()
    ball0.move_ball()

    # Trovo la posizione della palla e capisco se ha toccato il limite alto o basso

    y_ball = ball0.palla[0].ycor()
    x_ball = ball0.palla[0].xcor()
    angle = ball0.palla[0].heading()

    if (((y_ball >= 300 and (angle < 90 or angle > 270)) or
         (y_ball >= 300 and (angle > 90 or angle < 270))) or
            (y_ball <= -300 and (angle < 90 or angle > 270)) or
            (y_ball <= -300 and (angle > 90 or angle < 270))):
        ball0.palla[0].setheading(angle*-1)

    # controllo se ha colpito una racchetta

    pos_pad1 = [x.pos() for x in pad1.segments]
    pos_pad2 = [x.pos() for x in pad2.segments]

    rimb(pos_pad1, ball0.palla[0])
    rimb(pos_pad2, ball0.palla[0])

    # controllo se ha colpito il limite e aumento lo score relativo

    if x_ball >= 570 or x_ball <= -570:
        ball0.palla[0].goto(0, 0)
        ball0.palla[0].setheading(ball0.palla[0].heading() + 180)
        if x_ball >= 570:
            scoreb.increase1()
        if x_ball <= -570:
            scoreb.increase2()

    if scoreb.valore1 == 5 or scoreb.valore2 == 5:
        scoreb.end()
        games_on = False




screen.exitonclick()