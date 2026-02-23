sides = {}
users = {}

input_data = input()

while not input_data == "Lumpawaroo":
    if "|" in input_data:
        side, user = input_data.split(" | ")
        if user in users:
            input_data = input()
            continue
        if side not in sides:
            sides[side] = []
        
        sides[side].append(user)
        users[user] = side
    if ">" in input_data:
        user, side = input_data.split(" -> ")
        if side not in sides:
            sides[side] = []
        if user in users:
            sides[users[user]].remove(user)
           
        sides[side].append(user) 
        users[user] = side
        print(f"{user} joins the {side} side!")

    input_data = input()

new_line = "\n"
sides_filtered = {k: v for k, v in sides.items() if v}
[print(f"Side: {k}, Members: {len(v)}{new_line}{new_line.join(['! ' + m for m in v])}") for k, v in sides_filtered.items()]

# Old task condition for output:
#
# You should end your program when you receive the command "Lumpawaroo".
# At that point you should print each force side, ordered descending by forceUsers count, than ordered by name.
# For each side print the forceUsers, ordered by name.
# In case there are no forceUsers in a side, you shouldn`t print the side information.
#
# Solution for output according to the old condition
#
# sides_sorted = {k: sorted(v) for k, v in sorted(sides.items(), key=lambda item: (-len(item[1]), item[0])) if v}
# [print(f"Side: {k}, Members: {len(v)}{new_line}{new_line.join(['! ' + m for m in v])}") for k, v in sides_sorted.items()]