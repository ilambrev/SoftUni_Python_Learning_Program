n = int(input())

for number in range(1, n + 1):
    number_remainder = number
    digits_sum = 0

    while number_remainder > 0:
        digits_sum += number_remainder % 10
        number_remainder //= 10

    result = digits_sum == 5 or digits_sum == 7 or digits_sum == 11

    print(f'{number} -> {result}')