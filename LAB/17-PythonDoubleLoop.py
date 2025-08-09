num = int(input('Enter Your Loop'))
numTotal = []
for i in range(num):
    data = int(input('Enter Your Data: '))
    numTotal += [data]
print(numTotal)
numTotal.sort()
print(numTotal)