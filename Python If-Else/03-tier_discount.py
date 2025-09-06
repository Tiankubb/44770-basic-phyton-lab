amount = float(input("Enter purchase amount: "))
if amount > 2000:
    discount = 0.15  
elif amount > 1000:
    discount = 0.10  
elif amount > 500:
    discount = 0.05  
else:
    discount = 0.00 
total = amount - (amount * discount) 
print(f"Total after discount: {total:.2f} baht") 