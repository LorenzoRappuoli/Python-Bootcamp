from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# inzializzo il serpente

snake = Snake(0, 0)
food = Food()
score = Scoreboard()


# schermo e movimenti

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# gioco

games_on = True

while games_on:
    screen.update()
    time.sleep(0.1)

    # Movimento continuo in avanti

    snake.move()


    # Collisione con il cibo

    if snake.segments[0].distance(food) < 10:
        score.increase()
        food.refresh()
        snake.extend()

    # Collisione con il muro

    if (snake.segments[0].xcor() >= 290) or (snake.segments[0].xcor() <= -290) or (snake.segments[0].ycor() >= 290) or (snake.segments[0].ycor() <= -290):
        print("Lost")
        score.end()
        games_on = False

    # Collisione con parti del serpente

    for n in snake.segments[1:]:
        if n.pos() == snake.segments[0].pos():
            print("Lost")
            score.end()
            games_on = False





screen.exitonclick()