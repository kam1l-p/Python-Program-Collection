day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
dur = int(input("Enter the duration of the call (in minutes): "))
    
bill = 0
cost = 0
    
if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr":
    if time >= 530 and time <= 2100:
        bill = 0.55
        cost = round(bill * dur, 1)
        print("This call will cost", "$" + str(cost))
    else:
        bill = 0.35
        cost = round(bill * dur, 1)
        print("This call will cost", "$" + str(cost))
else:
    bill = 0.1
    cost = round(bill * dur, 1)
    print("This call will cost", "$" + str(cost))