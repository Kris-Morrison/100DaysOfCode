from turtle import Screen
from Paddle import Paddle

# Creating the screen to play on
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("Black")
screen.title("PONG")

#Paddle 1
paddle = Paddle()

screen.exitonclick()
