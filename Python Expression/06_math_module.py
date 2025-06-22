import math
x1, y1, x2, y2 = map(int, input("Enter coordinates x1 y1 x2 y2: ").split())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distance:.1f}")
