import math

a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))
print("")
    
if a == 0.0 and b == 0.0 and c == 0.0:
    print("This equation has infinite solution")
elif a == 0.0 and b == 0.0:
    print("This equation has no solution")   
elif ((b ** 2) - (4 * a * c)) < 0:
    print("This equation has no real solution")
else:   
    eq = (-1 * b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    eq2 = (-1 * b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    if eq == eq2:
        print("This equation has 1 solution: x =", eq)
    else:
        print("This equation has 2 solutions: x =", eq, "and x =", eq2)