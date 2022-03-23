import turtle
from turtle import Turtle, Screen
import random
from Colors import color_choice

# Fixed variables in the code and objects
turtle.colormode(255)
screen = Screen()
Tim = Turtle()

#Turtle pen attributes
y_axis = 230
Tim.speed("fastest")
Tim.pensize(20)
rgb_list = color_choice()

#Drawing of the spots in rows and columns
for _ in range(10):
    y_axis -= 30
    Tim.penup()
    Tim.goto(-230, y_axis)

    for spots_in_row in range(10):
        number = random.randint(0, 35)
        tuple_color = rgb_list[number]
        Tim.pencolor(tuple_color)
        Tim.pendown()
        Tim.forward(2)
        Tim.penup()
        Tim.forward(30)

screen.exitonclick()


