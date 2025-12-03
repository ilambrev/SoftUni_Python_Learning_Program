wagons = int(input())

train = [0] * wagons

command = input()

while not command == "End":
    command_parts = command.split()

    command_type = command_parts[0]

    if command_type == "add":
        people = int(command_parts[1])
        train[-1] += people
    elif command_type == "insert":
        index = int(command_parts[1])
        people = int(command_parts[2])
        train[index] += people
    elif command_type == "leave":
        index = int(command_parts[1])
        people = int(command_parts[2])
        train[index] -= people
    
    command = input()

print(train)