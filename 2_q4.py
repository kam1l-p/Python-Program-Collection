v_days = int(input("Enter the number of days Vamshi has worked: "))
v_hours = int(input("Enter the number of hours Vamshi has worked: "))
v_min = int(input("Enter the number of minutes Vamshi has worked: "))
    
n_days = int(input("Enter the number of days Nishat has worked: "))
n_hours = int(input("Enter the number of hours Nishat has worked: "))
n_min = int(input("Enter the number of minutes Nishat has worked: "))
    
total_d = v_days + n_days
total_h = v_hours + n_hours
total_m = v_min + n_min
    
if total_h >= 24:
    total_d += total_h // 24
    total_h = total_h % 24
        
if total_m >= 60:
    total_h += total_m // 60
    total_m = total_m % 60
    
print("The total time both CAs worked together is:", total_d,"days,", total_h,"hours and", total_m, "minutes")