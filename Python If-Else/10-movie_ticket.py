age = int(input("Age: "))
day = int(input("Day: "))
ticket = 100
if (5 < day < 8):
    ticket = ticket+50
else:
    ticket = ticket+0

if( age < 13):
    print(ticket)
elif(13 >= age > 60):
    print(ticket+80)
else: 
    print(ticket + 20)
