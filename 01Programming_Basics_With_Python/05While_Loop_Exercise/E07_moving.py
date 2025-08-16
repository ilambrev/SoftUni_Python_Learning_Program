space_width_in_meters = int(input())
space_length_in_meters = int(input())
space_height_in_meters = int(input())

space_volume_in_cubic_meters = (space_width_in_meters
                                * space_length_in_meters
                                * space_height_in_meters)

box_size_in_cubic_meters = 1

space_filled = 0

input_line = input()

while input_line != 'Done':
    boxes_count = int(input_line)
    space_filled += boxes_count * box_size_in_cubic_meters

    if space_filled > space_volume_in_cubic_meters:
        break

    input_line = input()

difference = space_volume_in_cubic_meters - space_filled

if difference >= 0:
    print(f'{difference} Cubic meters left.')
else:
    print(f'No more free space! You need {-difference} Cubic meters more.')