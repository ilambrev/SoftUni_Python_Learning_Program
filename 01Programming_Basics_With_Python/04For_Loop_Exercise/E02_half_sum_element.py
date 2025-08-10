from sys import maxsize

n = int(input())

max_num = -maxsize
numbers_sum = 0

for _ in range(1, n + 1):
    number = int(input())
    numbers_sum += number
    if number > max_num:
        max_num = number

numbers_sum -= max_num

if max_num == numbers_sum:
    print('Yes')
    print(f'Sum = {numbers_sum}')
else:
    print('No')
    print(f'Diff = {abs(numbers_sum - max_num)}')