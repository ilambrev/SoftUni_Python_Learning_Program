from math import pi

figure_type = input()
area = 0

if figure_type == 'square':
    square_side = float(input())
    area = square_side ** 2
elif figure_type == 'rectangle':
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    area = rectangle_side_a * rectangle_side_b
elif figure_type == 'circle':
    circle_radius = float(input())
    area = pi * circle_radius ** 2
elif figure_type == 'triangle':
    triangle_side = float(input())
    triangle_height = float(input())
    area = triangle_side * triangle_height / 2

print(f'{area:.3f}')