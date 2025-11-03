numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = abs(float(numbers[i]))

print(numbers)