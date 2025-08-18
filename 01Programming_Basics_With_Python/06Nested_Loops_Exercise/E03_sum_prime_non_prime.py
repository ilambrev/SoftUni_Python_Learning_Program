input_line = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while input_line != 'stop':
    number = int(input_line)

    if number < 0:
        print('Number is negative.')
        input_line = input()
        continue

    for divisor in range(2, number):
        if number % divisor == 0:
            non_prime_numbers_sum += number
            break
    else:
        prime_numbers_sum += number

    input_line = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')