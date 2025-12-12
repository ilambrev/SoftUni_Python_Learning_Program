numbers = [int(number) for number in input().split(".")]

addition = 1

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] + addition <= 9:
        numbers[i] += addition
        break
    else:
        numbers[i] = 0

print(*numbers, sep=".")