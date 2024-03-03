from turtle import Turtle, Screen
from random import choice, randint, random
from extract_color import main_colors

tim = Turtle()
tim.shape("turtle")

tim.speed("fastest")
tim.pen(pensize=1)


### square

#for _ in range(4):
#    tim.forward(100)
#    tim.left(90)
#
#tim.forward(100)


### dashed lines

#for _ in range(20):
#    tim.forward(10)
#    tim.pendown()
#    tim.forward(10)
#    tim.penup()
#

### Multiple shapes

#def move (t,angle):
#    for _ in range(angle):
#        t.right(360/angle)
#        t.forward(100)
#    return
#
#M = list(range(3,10))
#
#colors = ['black','green','blue','yellow','grey','purple','red','']
#
#for i in M:
#    tim.pen(pencolor=choice(colors), pensize=10)
#    move(tim,i)


### Random walk

#colors = ['black','green','blue','grey','purple','red',]

#for _ in range(randint(100,200)):
#    tup = (random(), random(), random())
#    tim.pencolor(tup)
#    if randint(1,2) == 1:
#        tim.right(360/randint(1,10))
#    else:
#        tim.left(360 / randint(1, 10))
#    tim.forward(randint(10,20))


###  Spirographic

#n = randint(0,100)
#for _ in range(int(n)):
#    tup = (random(), random(), random())
#    tim.pencolor(tup)
#    tim.circle(50)
#    tim.right(360/n)


########## PROJECT

tim.teleport(-450,-450)
tim.pen(pensize=10)
_flag = 0
_n = 20

for _ in range(_n):


    for _ in range(_n):
        tim.pendown()
        coord = [x/255 for x in choice(main_colors)]
        tim.pen(pencolor=(coord[0],coord[1],coord[2]))
        tim.dot(20,(coord[0],coord[1],coord[2]))
        tim.penup()
        tim.forward(60)

    if _flag%2 == 0:
        tim.left(90)
        tim.penup()
        tim.forward(60)
        tim.pendown()
        tim.left(90)
    else:
        tim.right(90)
        tim.penup()
        tim.forward(60)
        tim.pendown()
        tim.right(90)

    _flag +=1



screen = Screen()
screen.exitonclick()