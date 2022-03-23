import random


def card_name_number(card,player):
    if card == "J" or card == "Q" or card == "K":
        card = 10 
    elif card =="A" and player == "player":
        card = input("You got an ACE, would you like to choose '1' or '11' ? \n")
    elif card == "A":
        A_value = [1,11]
        card = random.choice(A_value)

    return card

def hand(player): 
    cards = [2,3,4,5,6,7,8,9,"J","Q","K","A"]
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    if player == "player":
        print(f"your been drawn: \n {card1} , {card2}")
    final_card1 = card_name_number(card1, player)
    final_card2 = card_name_number(card2, player)
    if player == "dealer" and final_card1 == "A" or final_card2 == "A":
        A_value = [1,11]
        if final_card1 == "A":
            final_card1 == random.choice(A_value)
        if final_card2 == "A":
            final_card2 == random.choice(A_value)
    total = int(final_card1) + int(final_card2)
    
    if player == "player":
        print(f"you have a value of: {total}")
    elif player == "dealer":
        print(f"dealer has been drawn: \n {card1} , {card2} \n He has a total: {total}")
    return total
    
def additional_hand(total, player):
    cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    card1 = random.choice(cards)
     
    if player == "player":
        final_card_add = card_name_number(card1, player)
        total += int(final_card_add)
        print(f"Your have been HIT with: {card1}") 
        print(f"Your value is now: {total}")
        if total > 21: 
            print ("Your BUST!")
    elif player == "dealer":
        final_card_add = card_name_number(card1, player)
        if card1 == "A":
            total += 11 
            if total > 21:
                total -= 10 
        if card1 !="A":
            total += int(final_card_add)
        print(f"Dealer has 'HIT', his card is {card1} and has a new total of: {total}")
        if total  > 21: 
            print("Dealar has gone BUST!")
    return total

player1 = 0 
dealer = 0 

#Players hand being played
player1 = hand("player")
stick_hit = input("would you like to 'hit' or 'stick' \n")
while stick_hit == "hit":
    player1 = additional_hand(player1, "player")
    stick_hit = input("would you like to 'hit' or 'stick' \n")

#dealers hand being played
dealer = hand("dealer")
while dealer < 17:
    dealer = additional_hand(dealer, "dealer")
    
        
#Who is the winner !
#print(player1)
#print(dealer)
if player1 <= 21 and dealer > 21:
    print("Your the winner! ")
elif player1 > 21 and dealer <= 21:
    print("You have lost against the dealer!  ")
elif player1 > dealer and player1 <= 21 and dealer <=21:
    print("Your the winner! ")
elif player1 < dealer and dealer <= 21 and player1 <= 21: 
    print("You have lost against the dealer! ")
elif player1 == dealer and player1 <21 and dealer <21:
    print("You have a draw! ")

