number = int(input())

isNumberPrime = True

for i in range(2, int(number / 2) + 1):
    if number % i == 0:
        isNumberPrime = False
        break

print(isNumberPrime)