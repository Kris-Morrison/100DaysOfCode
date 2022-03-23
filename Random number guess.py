import random

def loss_life(lifes):
    lifes -=1
    return lifes

real_num = random.randint(1,100)

mode = input("What level would you like to choose? 'easy' or 'hard'\n")

if mode == "easy":
    lifes = 10 
elif mode == "hard":
    lifes = 5 

while lifes !=0:
    win = "False"
    guess_num = int(input("Guess what the random number is? \n"))
    
    if guess_num > real_num:
        print("You have guessed too high! lost a life!")
        lifes = loss_life(lifes)
    elif guess_num < real_num:
        print("You have guessed too low! lost a life!")
        lifes = loss_life(lifes)
    elif guess_num == real_num:
        lifes = 0
        win = "True"
    print (f"You have {lifes} lifes remaining.")

if win == "True":
    print("You sucesfully guessed the number")
else:
    print("Your out of lifes and have lost!")

