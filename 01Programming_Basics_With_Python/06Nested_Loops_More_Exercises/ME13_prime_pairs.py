first_pair_initial_value = int(input())
second_pair_initial_value = int(input())
first_pair_initial_and_final_values_difference = int(input())
second_pair_initial_and_final_values_difference = int(input())

for first_pair in range(first_pair_initial_value, first_pair_initial_value + first_pair_initial_and_final_values_difference + 1):
    is_first_pair_simple = True

    for divisor in range(2, first_pair):
        if first_pair % divisor == 0:
            is_first_pair_simple = False
            break

    if not is_first_pair_simple:
        continue

    for second_pair in range(second_pair_initial_value, second_pair_initial_value + second_pair_initial_and_final_values_difference + 1):
        is_second_pair_simple = True

        for divisor in range(2, second_pair):
            if second_pair % divisor == 0:
                is_second_pair_simple = False
                break

        if not is_second_pair_simple:
            continue

        print(f'{first_pair}{second_pair}')