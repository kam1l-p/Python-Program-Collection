import random
play = str(input("Would you like to play 'Twenty-One'? [y/n] "))
while play != "y" and play != "n":
    play = input("Would you like to play 'Twenty-One'? [y/n] ")

if play == "y":
    card1 = random.randint(1,11)
    card2 = random.randint(1,11)
    print("Your cards are worth", card1, "and", str(card2) + ".")
    
    third = str(input("Would you like another card? [y/n] "))
    while third != "y" and third != "n":
        third = input("Would you like another card? [y/n] ")
    
    if third == "y":
        card3 = random.randint(1,11)
        print("Your score is", str(card1 + card2 + card3) + "!")
        score = card1 + card2 + card3
    else:
        print("Your score is", str(card1 + card2) + "!")
        score = card1 + card2
    
    opp = random.randint(0,100)
    while opp < 3 or opp > 33:
        opp = random.randint(0,100)
    
    print("Your opponent's score is", str(opp) + "!")
    
    if (opp > 21 and score > 21) or opp == score:
        print("It's a draw!")
    elif score == 21 or (opp > 21 or (score > opp and score <= 21)):
        print("You win! Your score was", str(score) + ".")
    elif opp == 21 or (score > 21 or (opp > score and opp <= 21)):
        print("Your opponent wins! Their score was", str(opp) + ".")
        
else:
    print("Thank you for playing!")