interval_start = int(input())
interval_end = int(input())

for first_digit in range(interval_start, interval_end + 1):
    for second_digit in range(interval_start, interval_end + 1):
        for third_digit in range(interval_start, interval_end + 1):
            for fourth_digit in range(interval_start, interval_end + 1):
                firs_condition = (first_digit % 2 == 0 and fourth_digit % 2 != 0
                                  or first_digit % 2 != 0 and fourth_digit % 2 == 0)
                second_condition = first_digit > fourth_digit
                third_condition = (second_digit + third_digit) % 2 == 0

                if firs_condition and second_condition and third_condition:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')