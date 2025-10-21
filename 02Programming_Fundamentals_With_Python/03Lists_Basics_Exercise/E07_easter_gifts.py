gifts_names = input().split()

command = input()

while not command == "No Money":
    command_parts = command.split()

    if command_parts[0] == "OutOfStock":
        gift_name = command_parts[1]

        for i in range(len(gifts_names)):
            if gifts_names[i] == gift_name:
                gifts_names[i] = "None"
    elif command_parts[0] == "Required":
        index = int(command_parts[2])
        mew_gift_name = command_parts[1]

        if (index >= 0 and index < len(gifts_names)):
            gifts_names[index] = mew_gift_name
    elif command_parts[0] == "JustInCase":
        gift_name_replacement = command_parts[1]
        gifts_names[-1] = gift_name_replacement

    command = input()

print(" ".join([name for name in gifts_names if not name == "None"]))