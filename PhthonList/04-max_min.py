n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
max_value = max(numbers)
min_value = min(numbers)
print(f"มากที่สุด: {max_value}")
print(f"น้อยที่สุด: {min_value}")