first_number = int(input())
second_number = int(input())
operator = input()

result = 0

if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
elif operator == '%':
    if second_number != 0:
        result = first_number % second_number

if operator == '+' or operator == '-' or operator == '*':
    type_of_result = ''
    if result % 2 == 0:
        type_of_result = 'even'
    else:
        type_of_result = 'odd'
    print(f'{first_number} {operator} {second_number} = {result} - {type_of_result}')
elif operator == '/' or operator == '%':
    formated_result = ''
    if operator == '/':
        formated_result = f'{result:.2f}'
    else:
        formated_result = f'{result}'
    if second_number != 0:
        print(f'{first_number} {operator} {second_number} = {formated_result}')
    else:
        print(f'Cannot divide {first_number} by zero')