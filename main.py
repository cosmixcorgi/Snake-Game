from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=620, height=660)
screen.bgcolor('#0d0d0d')
screen.title("Snake")
screen.tracer(0)


def draw_background():
    bg = Turtle()
    bg.hideturtle()
    bg.speed(0)
    bg.penup()

    bg.pensize(1)
    bg.color('#1c1c2e')
    for x in range(-280, 281, 20):
        bg.goto(x, -280)
        bg.pendown()
        bg.goto(x, 280)
        bg.penup()
    for y in range(-280, 281, 20):
        bg.goto(-280, y)
        bg.pendown()
        bg.goto(280, y)
        bg.penup()

    bg.pensize(3)
    bg.color('#00FF41')
    bg.goto(-290, -290)
    bg.pendown()
    bg.goto(290, -290)
    bg.goto(290, 290)
    bg.goto(-290, 290)
    bg.goto(-290, -290)
    bg.penup()

    for cx, cy in [(-290, -290), (290, -290), (290, 290), (-290, 290)]:
        bg.goto(cx, cy)
        bg.dot(14, '#00FF41')


draw_background()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
frame = 0

while game_is_on:
    screen.update()
    delay = max(0.05, 0.1 - scoreboard.score * 0.002)
    time.sleep(delay)

    snake.move()
    snake.update_colors()
    food.animate(frame)
    frame += 1

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
