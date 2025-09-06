age = int(input("Enter age: "))
day = int(input("Enter day of week (1-7): "))

if age < 13:
    price = 100
elif age <= 60: 
    price = 180
else:
    price = 120

if day == 6 or day == 7: 
    price += 50
print(f"Total ticket price: {price} baht")