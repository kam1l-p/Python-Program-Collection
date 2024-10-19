import random, math

hpmax = int(input("Enter the max health of this Pokémon: "))
hpcur = random.randint(1, hpmax)
ball = random.randint(1, 255)
    
eq = math.floor((hpmax * 255 * 4) / (hpcur * ball))
rd = random.randint(1, 254)
    
if eq >= rd:
    print("You've caught the Pokémon!")
else:
    print("Oh no! The Pokémon broke free!")