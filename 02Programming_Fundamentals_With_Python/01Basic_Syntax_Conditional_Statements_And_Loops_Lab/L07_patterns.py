number = int(input())

for i in range(1, number * 2):
    if i <= number:
        print('*' * i)
    else:
        print('*' * (2 * number - i))