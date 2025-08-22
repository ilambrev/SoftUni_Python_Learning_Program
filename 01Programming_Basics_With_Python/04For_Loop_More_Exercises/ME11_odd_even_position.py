n = int(input())

odd_sum = 0.0
odd_min = None
odd_max = None
even_sum = 0.0
even_min = None
even_max = None

for i in range(1, n + 1):
    number = float(input())

    if i == 1:
        odd_min = number
        odd_max = number

    if i == 2:
        even_min = number
        even_max = number

    if i % 2 != 0:
        odd_sum += number

        if number > odd_max:
            odd_max = number

        if number < odd_min:
            odd_min = number
    else:
        even_sum += number

        if number > even_max:
            even_max = number

        if number < even_min:
            even_min = number

if odd_min:
    odd_min = f'{odd_min:.2f}'
else:
    odd_min = 'No'

if odd_max:
    odd_max = f'{odd_max:.2f}'
else:
    odd_max = 'No'

if even_min:
    even_min = f'{even_min:.2f}'
else:
    even_min = 'No'

if even_max:
    even_max = f'{even_max:.2f}'
else:
    even_max = 'No'

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={odd_min},')
print(f'OddMax={odd_max},')
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={even_min},')
print(f'EvenMax={even_max}')