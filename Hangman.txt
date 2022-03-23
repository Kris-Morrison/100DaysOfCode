import random
import word_list
import hangman_artwork
from re import A 


print(hangman_artwork.logo)


number = random.randint(0,2)
word = word_list.word_list[number]
length = len(word)
#print(length)
display = ["_"]* length
print(display)
letter_list = list(word)
#print(letter_list)
life = 6


#print(letter_guess)
while life > 0 or display == letter_list:
    result = "False"
    letter_guess = input("Please, guess a letter?").lower()
    for letter in letter_list:
        if letter_guess == letter:
            
            result = "True"
            for item in range (0,length):
                character = letter_list[item]
                if character == letter_guess:
                    display[item] = letter_guess
            
    if result == "False":
        life -= 1 
        print(hangman_artwork.stages[life])
        print("This is not a letter in the word! You have lost a life.")
        #print(result)
        #print(life)
        print(display)
    elif result == "True":
        #print(result)
        #print(life)
        print(display)  
        

    if life == 0:
        print ("Game Over")
    elif display == letter_list:
        print ("You Win")