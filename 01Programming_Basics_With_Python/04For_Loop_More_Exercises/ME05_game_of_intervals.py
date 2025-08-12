turns_count = int(input())

numbers_from_0_to_9_count = 0
numbers_from_10_to_19_count = 0
numbers_from_20_to_29_count = 0
numbers_from_30_to_39_count = 0
numbers_from_40_to_50_count = 0
invalid_numbers_count = 0
points = 0.0

for _ in range(turns_count):
    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.2
        numbers_from_0_to_9_count += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        numbers_from_10_to_19_count += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        numbers_from_20_to_29_count += 1
    elif 30 <= number <= 39:
        points += 50
        numbers_from_30_to_39_count += 1
    elif 40 <= number <= 50:
        points += 100
        numbers_from_40_to_50_count += 1
    else:
        points /= 2
        invalid_numbers_count += 1

numbers_from_0_to_9_percentage = 100 * numbers_from_0_to_9_count / turns_count
numbers_from_10_to_19_percentage = 100 * numbers_from_10_to_19_count / turns_count
numbers_from_20_to_29_percentage = 100 * numbers_from_20_to_29_count / turns_count
numbers_from_30_to_39_percentage = 100 * numbers_from_30_to_39_count / turns_count
numbers_from_40_to_50_percentage = 100 * numbers_from_40_to_50_count / turns_count
invalid_numbers_percentage = 100 * invalid_numbers_count / turns_count

print(f'{points:.2f}')
print(f'From 0 to 9: {numbers_from_0_to_9_percentage:.2f}%')
print(f'From 10 to 19: {numbers_from_10_to_19_percentage:.2f}%')
print(f'From 20 to 29: {numbers_from_20_to_29_percentage:.2f}%')
print(f'From 30 to 39: {numbers_from_30_to_39_percentage:.2f}%')
print(f'From 40 to 50: {numbers_from_40_to_50_percentage:.2f}%')
print(f'Invalid numbers: {invalid_numbers_percentage:.2f}%')