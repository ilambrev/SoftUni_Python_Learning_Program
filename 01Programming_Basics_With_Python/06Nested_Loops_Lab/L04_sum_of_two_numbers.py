interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_number = 0
is_combination_found = False

for first_number in range(interval_start, interval_end + 1):
    for second_number in range(interval_start, interval_end + 1):
        combination_number += 1
        
        if first_number + second_number == magic_number:
            print(f'Combination N:{combination_number} ({first_number} + {second_number} = {magic_number})')
            is_combination_found = True
            break
            
    if is_combination_found:
        break
    
else:
    print(f'{combination_number} combinations - neither equals {magic_number}')