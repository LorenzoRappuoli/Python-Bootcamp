from turtle import Turtle, Screen, textinput
from random import randint

screen = Screen()
screen.setup(1000,1000)

def initial(t,x,y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    return

def move(t, n):
    t.forward(n)

user_bet = screen.textinput("Bet", "Which turtle is going to win this race?")

race_trace = Turtle()
race_trace.penup()
race_trace.setposition(300,400)
race_trace.right(90)
race_trace.pendown()
race_trace.forward(900)

tim = Turtle()
mark = Turtle()
jon = Turtle()




turtle = [tim, mark, jon]
colors = ["blue", "green", "red"]

for i in range(len(turtle)):
    turtle[i].pencolor(colors[i])
    initial(turtle[i], -200, 100 - 100*i)


percorso = [0,0,0]

while percorso[0] < 350 or percorso[1] < 350 or percorso[2] < 350:
    for i in range(len(turtle)):
        m = randint(0,100)
        move(turtle[i], m)
        percorso[i] += m



screen.exitonclick()