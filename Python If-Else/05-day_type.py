day = int(input("Enter day number (1-7): "))

if 1 <= day <= 5:  
    print("Weekday") 
elif 6 <= day <= 7: 
    print("Weekend") 
else:
    print("Invalid day number. Please enter 1-7.")  