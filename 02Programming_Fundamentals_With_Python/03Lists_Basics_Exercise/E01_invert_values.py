numbers_string = input()

numbers = numbers_string.split()

for i in range(len(numbers)):
    numbers[i] = -(int(numbers[i]))

print(numbers)