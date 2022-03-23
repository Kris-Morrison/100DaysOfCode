from turtle import Screen
from Snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Making of the snake body for the start of the game and controlling
snake = Snake()
food = Food()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.position[0].distance(food) < 15:
        food.re_move()
        snake.extend()
        scoreboard.increase_score()

    if snake.position[0].xcor() > 290 or snake.position[0].xcor() < -290 or snake.position[0].ycor() > 290 or \
            snake.position[0].ycor() < -290:
        scoreboard.gameover()
        game_is_on = False

    for segment in snake.position[1:]:
        if snake.position[0].distance(segment) < 3:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
