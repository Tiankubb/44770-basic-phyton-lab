year = int(input("Enter Year: "))

if(year%100 ==0):
    print("Not Leap Year")
if(year%400 ==0):
    print("Leap Year")
else: 
    print("Not Leap Year")