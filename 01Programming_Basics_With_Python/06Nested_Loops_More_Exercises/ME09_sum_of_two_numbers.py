interval_begin = int(input())
interval_end = int(input())
magic_number = int(input())

combination_counter = 0
is_combination_found = False

for first_number in range(interval_begin, interval_end + 1):
    for second_number in range(interval_begin, interval_end + 1):
        combination_counter += 1

        if first_number + second_number == magic_number:
            print(f'Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})')
            is_combination_found = True
            break
    
    if is_combination_found:
        break

if not is_combination_found:
    print(f'{combination_counter} combinations - neither equals {magic_number}')