from math import ceil

numbers = [int(number) for number in input().split(", ")]

result = []

for i in range(1, ceil(max(numbers) / 10) + 1):
    group = [number for number in numbers if ceil(number / 10) == i]

    result.append(group)

for i in range(len(result)):
    print(f"Group of {(i + 1) * 10}'s: {result[i]}")