n = int(input())
count = 0
for _ in range(n):
    num = int(input())
    if num > 50:
        count += 1
print(f"จำนวนที่มากกว่า 50: {count}")   