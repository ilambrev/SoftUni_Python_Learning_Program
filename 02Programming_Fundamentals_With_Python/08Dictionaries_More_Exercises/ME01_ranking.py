contests = {}

input_data = input()

while not input_data == "end of contests":
    contest, password = input_data.split(":")
    contests[contest] = password
    
    input_data = input()

users = {}

input_data = input()

while not input_data == "end of submissions":
    contest, password, username, points = input_data.split("=>")

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}
        
        if contest not in users[username] or users[username][contest] < int(points):
            users[username][contest] = int(points)

    input_data = input()

new_line = "\n"

users_by_points = {k: sum(v.values()) for k, v in sorted(users.items(), key=lambda item: -sum(item[1].values()))}
winner = max(users_by_points, key=users_by_points.get)
users_sorted = {k: v for k, v in sorted(users.items(), key=lambda item: item[0])}

print(f"Best candidate is {winner} with total {users_by_points[winner]} points.")
print("Ranking:")

for user, contests in users_sorted.items():
    print(f"{user}{new_line}{new_line.join(['#  ' + k + ' -> ' + str(v) for k, v in sorted(contests.items(), key=lambda item: -item[1])])}")