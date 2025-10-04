factor = int(input())
count = int(input())

numbers = []

for i in range(0, count):
    numbers.append(i * factor + factor)

print(numbers)