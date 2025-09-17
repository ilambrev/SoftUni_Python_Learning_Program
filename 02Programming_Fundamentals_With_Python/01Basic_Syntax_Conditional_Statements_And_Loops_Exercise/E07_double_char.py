command = input()

while not command == 'End':
    if command == 'SoftUni':
        command = input()
        continue

    result_string = ''

    for char in command:
        result_string += char * 2

    print(result_string)

    command = input()