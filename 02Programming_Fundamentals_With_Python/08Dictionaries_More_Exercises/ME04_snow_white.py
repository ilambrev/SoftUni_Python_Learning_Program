dwarfs = {}

input_data = input()

while not input_data == "Once upon a time":
    name, hat_color, physics = input_data.split(" <:> ")
    physics = int(physics)

    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
    
    if name not in dwarfs[hat_color] or physics > dwarfs[hat_color][name]:
        dwarfs[hat_color][name] = physics

    input_data = input()

dwarfs_list = []

for color, dwarfs_data in dwarfs.items():
    for name in dwarfs_data:
        dwarfs_list.append([color, name, dwarfs_data[name], len(dwarfs_data)])

dwarfs_list_sorted = sorted(dwarfs_list, key=lambda d: (-d[2], -d[3]))

[print(f"({d[0]}) {d[1]} <-> {d[2]}") for d in dwarfs_list_sorted]