xp = float(input("Enter this user's current XP: "))
lvl = 0
    
if xp < 15:
    lvl = 1
    print("Level", lvl, "Player (XP:", str(xp) + ")")
elif xp >= 15 and xp <= 24.99:
    lvl = 2
    print("Level", lvl, "Player (XP:", str(xp) + ")")
elif xp >= 25 and xp <= 29.99:
    lvl = 3
    print("Level", lvl, "Player (XP:", str(xp) + ")")
elif xp >= 30 and xp <= 39.99:
    lvl = 4
    print("Level", lvl, "Player (XP:", str(xp) + ")")
elif xp >= 40 and xp <= 60:
    lvl = 5
    print("Level", lvl, "Player (XP:", str(xp) + ")")
else:
    print("ERROR: Please enter a valid XP value.")