from math import floor

cake_width_in_cm = int(input())
cake_height_in_cm = int(input())

piece_size = 1
cake_pieces = floor(cake_width_in_cm * cake_height_in_cm / piece_size)

while True:
    input_line = input()

    if input_line == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break

    pieces_needed = int(input_line)

    if cake_pieces >= pieces_needed:
        cake_pieces -= pieces_needed
    else:
        missing_pieces = pieces_needed - cake_pieces
        print(f'No more cake left! You need {missing_pieces} pieces more.')
        break