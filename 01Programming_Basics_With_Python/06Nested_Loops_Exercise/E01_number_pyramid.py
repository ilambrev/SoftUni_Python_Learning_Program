n = int(input())

numbers_counter = 1
cols_counter = 0
result = ''

while numbers_counter <= n:
    cols_counter += 1
    current_counter = numbers_counter

    for i in range(cols_counter):
        result += str(current_counter + i)
        numbers_counter += 1

        if numbers_counter > n:
            break

        if i < current_counter - 1:
            result += ' '

    if numbers_counter <= n:
        result += '\n'

print(result)