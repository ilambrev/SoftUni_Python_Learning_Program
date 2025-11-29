from math import sqrt, floor

def find_closest_point(x1, y1, x2, y2):
    distance1 = sqrt(x1 ** 2 + y1 ** 2)
    distance2 = sqrt(x2 ** 2 + y2 ** 2)

    if distance2 < distance1:
        return [floor(x2), floor(y2), floor(x1), floor(y1)]
    else:
        return [floor(x1), floor(y1), floor(x2), floor(y2)]

def calculate_line_length(l_x1, l_y1, l_x2, l_y2):
    return sqrt((max(l_x1, l_x2) - min(l_x1, l_x2)) ** 2 + (max(l_y1, l_y2) - min(l_y1, l_y2)) ** 2)

l1_x1 = float(input())
l1_y1 = float(input())
l1_x2 = float(input())
l1_y2 = float(input())
l2_x1 = float(input())
l2_y1 = float(input())
l2_x2 = float(input())
l2_y2 = float(input())

line1 = calculate_line_length(l1_x1, l1_y1, l1_x2, l1_y2)
line2 = calculate_line_length(l2_x1, l2_y1, l2_x2, l2_y2)

result = []

if line2 > line1:
    result = find_closest_point(l2_x1, l2_y1, l2_x2, l2_y2)
else:
    result = find_closest_point(l1_x1, l1_y1, l1_x2, l1_y2)

print(f"{result[0], result[1]}{result[2], result[3]}")