n = int(input())

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):
                first_sum = first_digit + second_digit
                second_sum = third_digit + fourth_digit

                if first_sum == second_sum and n % first_sum == 0:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')