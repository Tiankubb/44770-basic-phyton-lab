x = int(input("number "))
y = int(input("number "))
z = int(input("number "))

if(x >= y and x >= z):
    print(x)
elif(y >= x and y >= z):
    print(y)
else:
    print(z)