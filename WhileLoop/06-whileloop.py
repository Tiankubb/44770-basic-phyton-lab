def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

while True:
  print("1. pluss 2 digits")
  print("2. minus 2 digits")
  print("3. x 2 digits")
  print("4. out")
  choice = int(input())
  
  if choice == 4:
    print("program endded")
    break

  a = int(input())
  b = int(input())

  if choice == 1:
    print("ผลลัพธ์:",add(a,b))
  elif choice == 2:
    print("ผลลัพธ์:",sub(a,b))
  elif choice == 3:
    print("ผลลัพธ์:",mul(a,b))