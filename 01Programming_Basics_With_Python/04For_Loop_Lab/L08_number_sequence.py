n = int(input())

min_number = 0
max_number = 0

for i in range(0, n):
    number = int(input())
    if i == 0:
        min_number = number
        max_number = number
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print('Max number:', max_number)
print('Min number:', min_number)