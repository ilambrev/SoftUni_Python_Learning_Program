floors_count = int(input())
rooms_per_floor = int(input())

for floor in range(floors_count, 0, -1):
    rooms = ''

    for room in range(rooms_per_floor):
        room_type = ''

        if floor == floors_count:
            room_type = 'L'
        elif floor % 2 == 0:
            room_type = 'O'
        else:
            room_type = 'A'

        rooms += f'{room_type}{floor}{room}'

        if room < rooms_per_floor - 1:
            rooms += ' '

    print(rooms)