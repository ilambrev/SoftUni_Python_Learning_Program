first_number = int(input())
second_number = int(input())

result = ''

for number in range(first_number, second_number + 1):
    numbers_on_even_position_sum = 0
    numbers_on_odd_position_sum = 0

    current_number = str(number)

    for i in range(6):
        digit = int(current_number[i])
        if i % 2 == 0:
            numbers_on_even_position_sum += digit
        else:
            numbers_on_odd_position_sum += digit

    if numbers_on_even_position_sum == numbers_on_odd_position_sum:
        result += f'{current_number} '

if result:
    print(result.rstrip())