def find_even_numbers(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))

numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(find_even_numbers(numbers))