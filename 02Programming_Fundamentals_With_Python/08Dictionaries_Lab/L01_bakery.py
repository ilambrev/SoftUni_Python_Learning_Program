keys_values = input().split()

bakery = {}

for i in range(1, len(keys_values), 2):
    bakery[keys_values[i - 1]] = int(keys_values[i])

print(bakery)