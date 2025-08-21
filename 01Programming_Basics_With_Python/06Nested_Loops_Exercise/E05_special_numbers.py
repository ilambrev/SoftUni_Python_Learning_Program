n = int(input())

special_numbers = ''

for number in range(1111, 10000):
    current_number = number
    while current_number > 0:
        digit = current_number % 10
        if digit == 0 or n % digit != 0:
            break

        current_number //= 10
    else:
        special_numbers += f'{number} '

print(special_numbers.rstrip())