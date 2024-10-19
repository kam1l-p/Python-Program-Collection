import math

guests = int(input("Enter the number of guests: "))
slices = int(input("Enter the number of pizza slices each guest will eat: "))
    
pies = math.ceil((guests * slices) / 8)
rest = (pies * 8) - (guests * slices)

print()
print("Minimum number of whole large pizzas required:", pies)
print("Total number of large pizza slices needed:", guests * slices)
print("Number of large pizza slices left over:", rest)