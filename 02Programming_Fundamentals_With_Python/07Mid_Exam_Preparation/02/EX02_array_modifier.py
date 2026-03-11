numbers = [int(n) for n in input().split()]

command = input()

while not command == "end":
    command_parts = command.split()
    action = command_parts[0]
    index1 = int(command_parts[1]) if len(command_parts) > 1 else 0
    index2 = int(command_parts[2]) if len(command_parts) > 1 else 0

    if action == "swap":
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        numbers[index1] *= numbers[index2]
    elif action == "decrease":
        for i in range(len(numbers)):
            numbers[i] -= 1
    
    command = input()

print(", ".join(str(n) for n in numbers))