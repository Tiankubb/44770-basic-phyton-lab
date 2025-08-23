def show_table(n, limit):
    i = int(input("Number"))
    while i <= limit:
        print(f"{n} x {i} = {n * i}")
        i += 1

show_table(4, 3)
