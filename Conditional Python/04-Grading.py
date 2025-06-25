g = int(input("Grade Value: "))
if(g >= 80 and g <= 100):
    print("A")
elif(g >= 75 and g <= 79):
    print("B+")
elif(g >= 70 and g <= 74):
    print("B")
elif(g >= 65 and g <= 69):
    print("C+")
elif(g >= 60 and g <= 64):
    print("C")
elif(g >=55 and g <= 59):
    print("D+")
elif(g >= 50 and g <= 54):
    print("D")
elif(g == 0 and g <= 49):
    print("F")
else:
    print("Error")