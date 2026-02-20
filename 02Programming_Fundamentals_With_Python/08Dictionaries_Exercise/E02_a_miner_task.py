input_data = input()

resources = {}

while not input_data == "stop":
    resource = input_data
    quantity = int(input())

    if resource not in resources:
        resources[resource] = 0

    resources[resource] += quantity

    input_data = input()

[print(f"{key} -> {value}") for key, value in resources.items()]