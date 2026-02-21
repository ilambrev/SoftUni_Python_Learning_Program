phonebook = {}

input_data = input()

while "-" in input_data:
    name, phone = input_data.split("-")

    phonebook[name] = phone

    input_data = input()

for _ in range(int(input_data)):
    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")