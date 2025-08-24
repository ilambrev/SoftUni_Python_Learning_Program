n = int(input())

counter = n
numbers_sum = 0

while counter > 0:
    number = int(input())
    numbers_sum += number

    counter -= 1

average_number = numbers_sum / n

print(f'{average_number:.2f}')