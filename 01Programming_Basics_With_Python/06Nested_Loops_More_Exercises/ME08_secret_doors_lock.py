hundreds_upper_limit = int(input())
tens_upper_limit = int(input())
ones_upper_limit = int(input())

for hundred in range(2, hundreds_upper_limit + 1, 2):
    for ten in range(2, tens_upper_limit + 1):
        is_ten_simple_number = True

        for divisor in range(2, ten):
            if ten % divisor == 0:
                is_ten_simple_number = False
                break

        if not is_ten_simple_number:
            continue

        for one in range(2, ones_upper_limit + 1, 2):
            print(f'{hundred} {ten} {one}')