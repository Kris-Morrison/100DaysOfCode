import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_1 = input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
player_1_int = int(player_1)
if player_1_int >=3 or player_1_int <0: 
    print ("You entered an invalid number. You lose! ")
else:
    if player_1_int == 0:
    print(rock)
    player_hand = "rock"
    elif player_1_int == 1:
    print(paper)
    player_hand = "paper"
    elif player_1_int== 2:
    print(scissors) 
    player_hand = "scissors"

    print ("Computer chose:\n")
    computer_1 = random.randint(0,2)
    #print (computer_1)
    if computer_1 == 0:
        print(rock)
        computer_hand = "rock"
    elif computer_1 == 1:
    print(paper)
    computer_hand = "paper"
    elif computer_1 == 2:
    print(scissors)
    computer_hand = "scissors"
    
    #Player Wins
    if player_hand == "rock" and computer_hand == "scissors":
        print ("You win")
        
    if player_hand == "paper" and computer_hand == "rock":
        print ("You win")
        
    if player_hand == "scissors" and computer_hand == "paper":
        print ("You win")
        
    #Computer Wins 
    if computer_hand == "rock" and player_hand == "scissors":
        print ("You lose")
        
    if computer_hand == "paper" and player_hand == "rock":
        print ("You lose")
        
    if computer_hand == "scissors" and player_hand == "paper":
        print ("You lose")
        
    #Draw
    if player_hand == computer_hand :
        print ("Draw")