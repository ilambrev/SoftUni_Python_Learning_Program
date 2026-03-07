from string import ascii_uppercase

strings = input().split()

numbers = []

for string in strings:
    first_letter = string[0]
    second_letter = string[-1]
    number = int(string[1:-1])
    result = 0

    if first_letter in ascii_uppercase:
        result = number / (ascii_uppercase.find(first_letter) + 1)
    else:
        result = number * (ascii_uppercase.find(first_letter.upper()) + 1)

    if second_letter in ascii_uppercase:
        result = result - (ascii_uppercase.find(second_letter) + 1)
    else:
        result = result + (ascii_uppercase.find(second_letter.upper()) + 1)

    numbers.append(result)

print(f"{sum(numbers):.2f}")