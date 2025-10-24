numbers = input().split(", ")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

zeroes = []
other_numbers = []

for i in range(len(numbers)):
    if numbers[i] == 0:
        zeroes.append(numbers[i])
    else:
        other_numbers.append(numbers[i])

print(other_numbers + zeroes)