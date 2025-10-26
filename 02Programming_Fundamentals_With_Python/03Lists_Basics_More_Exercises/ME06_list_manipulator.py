numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

command = input()

while not command == "end":
    command_parts = command.split()

    if command_parts[0] == "exchange":
        index = int(command_parts[1])

        if index < 0 or index > len(numbers) - 1:
            print("Invalid index")
        elif index < len(numbers) - 1:
            numbers = numbers[index + 1:] + numbers[:index + 1]
    elif command_parts[0] == "max":
        element_type = command_parts[1]
        new_list = []

        if element_type == "even":
            for number in numbers:
                if number % 2 == 0:
                    new_list.append(number)
        elif element_type == "odd":
            for number in numbers:
                if not number % 2 == 0:
                    new_list.append(number)

        if len(new_list) == 0:
            print("No matches")
        else:
            print(len(numbers) - 1 - numbers[::-1].index(max(new_list)))
    elif command_parts[0] == "min":
        element_type = command_parts[1]
        new_list = []

        if element_type == "even":
            for number in numbers:
                if number % 2 == 0:
                    new_list.append(number)
        elif element_type == "odd":
            for number in numbers:
                if not number % 2 == 0:
                    new_list.append(number)

        if len(new_list) == 0:
            print("No matches")
        else:
            print(len(numbers) - 1 - numbers[::-1].index(min(new_list)))
    elif command_parts[0] == "first":
        elements_count = int(command_parts[1])
        element_type = command_parts[2]
        new_list = []

        if element_type == "even":
            for number in numbers:
                if number % 2 == 0:
                    new_list.append(number)
        elif element_type == "odd":
            for number in numbers:
                if not number % 2 == 0:
                    new_list.append(number)

        if elements_count > len(numbers):
            print("Invalid count")
        elif elements_count > len(new_list):
            print(new_list)
        else:
            print(new_list[:elements_count])
    elif command_parts[0] == "last":
        elements_count = int(command_parts[1])
        element_type = command_parts[2]
        new_list = []

        if element_type == "even":
            for number in numbers:
                if number % 2 == 0:
                    new_list.append(number)
        elif element_type == "odd":
            for number in numbers:
                if not number % 2 == 0:
                    new_list.append(number)

        if elements_count > len(numbers):
            print("Invalid count")
        elif elements_count > len(new_list):
            print(new_list)
        else:
            print(new_list[-elements_count:])

    command = input()

print(numbers)