control_value = int(input())

combinations_counter = 0
password = ''
result = ''

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):

                first_condition = ((first_digit * second_digit)
                                   + (third_digit * fourth_digit)) == control_value
                second_condition = first_digit < second_digit
                third_condition = third_digit > fourth_digit

                if first_condition and second_condition and third_condition:
                    combinations_counter += 1
                    number = f'{first_digit}{second_digit}{third_digit}{fourth_digit}'
                    result += f'{number} '

                    if combinations_counter == 4:
                        password = number

if result:
    print(result.rstrip())

if password:
    print(f'Password: {password}')

if combinations_counter < 4:
    print('No!')