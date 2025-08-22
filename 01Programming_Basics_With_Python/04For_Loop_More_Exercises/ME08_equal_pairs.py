n = int(input())

first_number = int(input())
second_number = int(input())

sum = first_number + second_number
is_sum_different = False
max_difference = 0

for _ in range(n - 1):
    first_number = int(input())
    second_number = int(input())

    current_sum = first_number + second_number

    if (current_sum != sum):
        is_sum_different = True
        difference = abs(current_sum - sum)
        sum = current_sum

        if (difference > max_difference):
            max_difference = difference

if is_sum_different:
    print(f'No, maxdiff={max_difference}')
else:
    print(f'Yes, value={sum}')