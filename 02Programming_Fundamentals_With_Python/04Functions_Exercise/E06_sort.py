def sort_numbers(numbers):
    return sorted(numbers)

numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(sort_numbers(numbers))