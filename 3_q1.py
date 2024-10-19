print("Welcome to the Lemonade Stand Profit Calculator!")
    
szn = input("Enter the current season (summer/other): ")
small = int(input("Enter the number of small cups of lemonade sold: "))
medium = int(input("Enter the number of medium cups of lemonade sold: "))
large = int(input("Enter the number of large cups of lemonade sold: "))
    
total_profit = 0
    
if szn == "summer":
    total_profit = (small * (2 - 1)) + (medium * (2.5 - 1.25)) + (large * (3 - 1.5))
    print("Total profit for the day in the summer :", "$" + str(total_profit))
else:
    total_profit = total_profit = (small * (1.5 - 0.75)) + (medium * (2 - 1)) + (large * (2.5 - 1.25))
    print("Total profit for the day in the rest of the year :", "$" + str(total_profit))