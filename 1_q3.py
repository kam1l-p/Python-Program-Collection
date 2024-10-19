print("Enter number of coins:")

quarters = int(input("Number of quarters: "))
dimes = int(input("Number of dimes: "))
nickels = int(input("Number of nickels: "))
pennies = int(input("Number of pennies: "))

total = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
dollars = total // 100
cents = total % 100

print("The total is", dollars, "dollar(s) and", cents, "cent(s)")