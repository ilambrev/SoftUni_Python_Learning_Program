first_player_name = input()
second_player_name = input()

first_player_score = 0
second_player_score = 0

command = input()


while command != 'End of game':
    first_player_card_value = int(command)
    second_player_card_value = int(input())

    difference = first_player_card_value - second_player_card_value

    if difference > 0:
        first_player_score += difference
    elif difference < 0:
        second_player_score += abs(difference)
    else:
        print('Number wars!')
        first_player_card_value = int(input())
        second_player_card_value = int(input())

        if first_player_card_value > second_player_card_value:
            print(f'{first_player_name} is winner with {first_player_score} points')
        else:
            print(f'{second_player_name} is winner with {second_player_score} points')

        break

    command = input()

else:
    print(f'{first_player_name} has {first_player_score} points')
    print(f'{second_player_name} has {second_player_score} points')