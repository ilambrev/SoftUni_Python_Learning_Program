tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
unused_volume_percentage = float(input())

volume_in_cm = (100 - unused_volume_percentage) * \
    tank_length * tank_width * tank_height / 100
volume_in_dm = volume_in_cm / 1000

print(volume_in_dm)