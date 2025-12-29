electrons_number = int(input())

result = []
i = 1

while electrons_number:
    shell_max_capacity = 2 * i ** 2

    if electrons_number > shell_max_capacity:
        result.append(shell_max_capacity)
        electrons_number -= shell_max_capacity
        i += 1
    else:
        result.append(electrons_number)
        electrons_number = 0

print(result)