numbers = input().split()
text = input()

indexes = []

for number in numbers:
    digits_sum = 0

    for digit in str(number):
        digits_sum += int(digit)

    indexes.append(digits_sum)

symbols = []

for symbol in text:
    symbols.append(symbol)

message = ""

for index in indexes:
    i = index % len(symbols)
    message += symbols[i]
    symbols.pop(i)

print(message)