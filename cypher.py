def encrypt(text, shift):
    new_word =""
    Letter = list(text)
    
    for character in Letter:
        if character in alphabet:
            position = alphabet.index(character)
            new_shift = position + shift
            if new_shift >= 25: 
                final_shift = new_shift % 25 
            else:
                final_shift = new_shift
            #print(final_shift)   
                new_letters = alphabet[final_shift]
                new_word += new_letters
        elif not character in alphabet:
            new_word += character
            
            #print (new_word)
    print (f"The encoded text is {new_word}")
    
def decrypt(text, shift):
    new_word =""
    Letter = list(text)
    
    for character in Letter:
            if character in alphabet:
                position = alphabet.index(character)
                new_shift = position - shift
                if new_shift < 0:
                    final_shift = new_shift % 25
                else:
                    final_shift = new_shift
                
                new_letters = alphabet[final_shift]
                new_word += new_letters
            elif not character in alphabet:
                new_word += character
            #print (new_word)
    print (f"The decode text is {new_word}")

import art 

print (art.logo)   
finish = "yes"
while finish == "yes":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
        
    finish = input ("Do you want to another word ? 'ues' or 'no'")
