from turtle import Turtle
import time

MOVE_FORWARD = 5
X_CORD = [-40, -20, 0]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        snake_locations = []
        for snake in range(0, 3):
            x_cord = X_CORD
            snake_body = Turtle()
            snake_body.penup()
            snake_body.color("white")
            snake_body.shape("square")
            snake_body.setx(x_cord[snake])
            snake_locations.append(snake_body)
            self.position = snake_locations

    def move(self):
        self.position[0].forward(10)
        for segments in range(len(self.position) - 1, 0, -1):
            new_x_cord = self.position[segments - 1].xcor()
            new_y_cord = self.position[segments - 1].ycor()
            self.position[segments].goto(new_x_cord, new_y_cord)
        self.position[0].forward(MOVE_FORWARD)

    def up(self):
        if self.position[0].heading() != DOWN:
            self.position[0].setheading(UP)
            self.position[0].forward(MOVE_FORWARD)

    def down(self):
        if self.position[0].heading() != UP:
            self.position[0].setheading(DOWN)
            self.position[0].forward(MOVE_FORWARD)

    def left(self):
        if self.position[0].heading() != RIGHT:
            self.position[0].setheading(LEFT)
            self.position[0].forward(MOVE_FORWARD)

    def right(self):
        if self.position[0].heading() != LEFT:
            self.position[0].setheading(RIGHT)
            self.position[0].forward(MOVE_FORWARD)

    def extend(self):
        snake_body = Turtle()
        snake_body.penup()
        snake_body.color("white")
        snake_body.shape("square")
        snake_body.goto(self.position[-1].position())
        self.position.append(snake_body)



