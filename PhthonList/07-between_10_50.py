n = int(input())
numbers = [int(input()) for _ in range(n)]
filtered = [num for num in numbers if 10 <= num <= 50]
print(f"ค่าที่อยู่ในช่วง 10-50: {filtered}")