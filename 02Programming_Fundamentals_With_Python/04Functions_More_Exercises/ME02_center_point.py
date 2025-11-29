from math import sqrt, floor

def find_closest_point(x1, y1, x2, y2):
    distance1 = sqrt(x1 ** 2 + y1 ** 2)
    distance2 = sqrt(x2 ** 2 + y2 ** 2)

    if distance2 < distance1:
        print(f"({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x1)}, {floor(y1)})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

find_closest_point(x1, y1, x2, y2)