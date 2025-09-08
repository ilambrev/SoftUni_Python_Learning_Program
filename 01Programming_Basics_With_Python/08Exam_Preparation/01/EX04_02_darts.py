player_name = input()

player_points = 301
successful_shots = 0
unsuccessful_shots = 0
command = input()

while command != 'Retire':
    field_type = command
    field_points = int(input())

    if field_type == 'Double':
        field_points *= 2
    elif field_type == 'Triple':
        field_points *= 3

    if field_points <= player_points:
        player_points -= field_points
        successful_shots += 1
    else:
        unsuccessful_shots += 1

    if player_points == 0:
        print(f'{player_name} won the leg with {successful_shots} shots.')
        break

    command = input()

else:
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')