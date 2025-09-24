input_lines_count = int(input())

water_tank_capacity = 255
liters_in_tank = 0

for _ in range(input_lines_count):
    liters_of_water = int(input())

    if liters_of_water > water_tank_capacity - liters_in_tank:
        print('Insufficient capacity!')
    else:
        liters_in_tank += liters_of_water

print(liters_in_tank)