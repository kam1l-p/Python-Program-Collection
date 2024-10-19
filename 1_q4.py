dollars = int(input("Enter amount of dollars: "))
cents = int(input("Enter amount of cents: "))
print(dollars, "dollars and", cents, "cents are:")
    
total = (dollars * 100) + cents
    
quarters = total // 25
total %= 25
dimes = total // 10
total %= 10
nickels = total // 5
pennies = total % 5
    
print(quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies")