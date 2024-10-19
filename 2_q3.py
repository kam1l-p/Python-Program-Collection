import math, random

ran = random.randint(1,20)
print("Random integer(1-20):", ran)
    
sq = round(math.sqrt(ran),2)
print("Square root of", ran, "is:", sq)
    
area = round(math.pi * (sq ** 2),2)
print("\nArea of a circle with radius", sq, "is:", area)