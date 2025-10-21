numbers_string = input()
n = int(input())

numbers = [int(number) for number in numbers_string.split()]
survival_numbers = sorted(numbers)[n:]

print(", ".join([str(number) for number in numbers if number in survival_numbers]))