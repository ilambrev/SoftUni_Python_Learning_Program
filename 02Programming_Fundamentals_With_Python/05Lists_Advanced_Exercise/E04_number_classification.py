numbers = [int(number) for number in input().split(", ")]
sep = ", "

print("Positive:", sep.join([str(number) for number in numbers if number >= 0]))
print("Negative:", sep.join([str(number) for number in numbers if number < 0]))
print("Even:", sep.join([str(number) for number in numbers if number % 2 == 0]))
print("Odd:", sep.join([str(number) for number in numbers if not number % 2 == 0]))