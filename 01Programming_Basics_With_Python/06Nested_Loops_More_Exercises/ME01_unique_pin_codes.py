first_digit_upper_limit = int(input())
second_digit_upper_limit = int(input())
third_digit_upper_limit = int(input())

for first_digit in range(2, first_digit_upper_limit + 1, 2):
    for second_digit in range(2, second_digit_upper_limit + 1):
        is_digit_prime = True

        for number in range(2, second_digit):
            if second_digit % number == 0:
                is_digit_prime = False
                break

        if is_digit_prime:
            for third_digit in range(2, third_digit_upper_limit + 1, 2):
                print(f'{first_digit} {second_digit} {third_digit}')