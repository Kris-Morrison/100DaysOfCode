from turtle import Screen, Turtle


def forward():
    tim.forward(10)


def back():
    tim.backward(10)


def clockwise():
    tim.right(10)


def anti_clockwise():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()..

tim = Turtle()
screen = Screen()
screen.listen()
# TODO 1. Forwards
screen.onkey(forward, "w")

# TODO 2. Backwards
screen.onkey(back, "s")

# TODO 3. Counter-Clockwise
screen.onkey(clockwise, "a")

# TODO 4. Clockwise
screen.onkey(anti_clockwise, "d")

# TODO 5. Clear screen
screen.onkey(clear, "c")

screen.exitonclick()
