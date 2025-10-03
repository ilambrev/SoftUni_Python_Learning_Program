n = int(input())

numbers = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

for i in range(len(numbers) - 1, -1, -1):
    number = numbers[i]
    
    if command == 'even' and not number % 2 == 0:
        numbers.pop(i)
    elif command == 'odd' and number % 2 == 0:
        numbers.pop(i)
    elif command == 'negative' and number >= 0:
        numbers.pop(i)
    elif command == 'positive' and number < 0:
        numbers.pop(i)

print(numbers)