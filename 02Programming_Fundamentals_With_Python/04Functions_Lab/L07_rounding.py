def round_numbers(numbers):
    rounded_numbers = []

    for number in numbers:
        rounded_numbers.append(round(float(number)))

    return rounded_numbers

numbers = input().split(" ")

print(round_numbers(numbers))