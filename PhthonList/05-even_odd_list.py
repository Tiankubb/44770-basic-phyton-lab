n = int(input())
even_numbers = []
odd_numbers = []
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(f"เลขคู่: {even_numbers}")
print(f"เลขคี่: {odd_numbers}")