def show_table(n, limit):
  i = 1
  while i <= limit:
    print(n,"x",i,"=",n*i)
    i = i+1
n = int(input("n = "))
limit = int(input("limit = "))
show_table(n,limit)