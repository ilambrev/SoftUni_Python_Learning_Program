def calculate_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial

first_number = int(input())
second_number = int(input())

result = calculate_factorial(first_number) / calculate_factorial(second_number)

print(f"{result:.2f}")