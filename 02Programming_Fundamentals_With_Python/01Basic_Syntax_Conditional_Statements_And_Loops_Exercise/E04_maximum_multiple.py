divisor = int(input())
boundary = int(input())

wanted_number = 0

for current_number in range(1, boundary + 1):
    if current_number % divisor == 0:
        wanted_number = current_number

print(wanted_number)