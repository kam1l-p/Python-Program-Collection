n = int(input("Please enter a positive integer: "))

for i in range(n):
    blank = " " * i
    star = "*" * (2 * (n - i) - 1)
    print(blank + star)

for i in range(1, n):
    blank = " " * (n - i - 1)
    star = "*" * (2 * (i + 1) - 1)
    print(blank + star)