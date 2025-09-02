wall_height = float(input())
wall_length = float(input())
roof_height = float(input())

window_area = 1.5 * 1.5
door_area = 1.2 * 2
walls_area = (wall_height * wall_height * 2
              + wall_length * wall_height * 2
              - window_area * 2
              - door_area)
roof_area = (wall_height * wall_length * 2
             + wall_height * roof_height)

green_paint_amount = walls_area / 3.4
red_paint_amount = roof_area / 4.3

print(f'{green_paint_amount:.2f}')
print(f'{red_paint_amount:.2f}')