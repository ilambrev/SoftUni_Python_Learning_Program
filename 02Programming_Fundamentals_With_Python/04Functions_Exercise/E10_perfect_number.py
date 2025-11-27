def is_number_perfect(number):
    sum = 0

    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            sum += i

    if number == sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())

print(is_number_perfect(number))