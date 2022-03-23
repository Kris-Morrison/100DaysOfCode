from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "green", "blue", "yellow", "purple", "orange"]
screen.title("Turtle Races!")
# Who will win the race ?
is_bet_on = False
guess_winner = screen.textinput(title="Who is the winner?", prompt='Who do you think will win? \n "red", "green", "blue", "yellow", "purple", "orange" ')


# Create all competers for the race
def turtle_maker(number, y_axis):
    turtle = Turtle()
    turtle.color(color[number])
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(x=-240, y=y_axis)
    return turtle


y_axis = [190,160,130,100,70,40,10]
turtle_list = []
for turtle_num in range(0, 6):
    y_axis_position = y_axis[turtle_num]
    turtle_list.append(turtle_maker(turtle_num, y_axis_position))


print(turtle_list)
# Race begins
if guess_winner:
    is_bet_on = True


while is_bet_on:
    for turtle in turtle_list:
        turtle_distance = random.randint(1,10)
        turtle.forward(turtle_distance)
        if turtle.xcor() >= 210:
            #print(turtle.color())
            is_bet_on = False
            if guess_winner == turtle.color():
                print(f"You are the winner! the {guess_winner} was the winner")
            else:
                color = turtle.pencolor()
                print(f"You lose! the {color} was the winner!")


screen.exitonclick()
