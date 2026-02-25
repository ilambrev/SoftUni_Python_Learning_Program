contests = {}
users = {}

input_data = input()

while not input_data == "no more time":
    username, contest, points = input_data.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = []
    
    if username not in contests[contest]:
        contests[contest].append(username)
    
    if username not in users:
        users[username] = {}
    
    if contest not in users[username]:
        users[username][contest] = 0
    
    if users[username][contest] < points:
        users[username][contest] = points

    input_data = input()

new_line = "\n"

contests_sorted = {k: sorted([[u, users[u][k]] for u in v], key=lambda p: (-p[1], p[0])) for k, v in contests.items()}
users_sorted = [[k, sum(v.values())] for k, v in sorted(users.items(), key=lambda item: (-sum(item[1].values()), item[0]))]

([print(f"{k}: {len(v)} participants{new_line}{new_line.join([str(i + 1) + '. ' + v[i][0] + ' <::> ' + str(v[i][1]) for i in range(len(v))])}") 
  for k, v in contests_sorted.items()])
print("Individual standings:")
[print(f"{str(i + 1) + '. ' + users_sorted[i][0] + ' -> ' + str(users_sorted[i][1])}") for i in range(len(users_sorted))]