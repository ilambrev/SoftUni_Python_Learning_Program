languages = {}
users = {}

input_data = input()

while not input_data == "exam finished":
    command_parts = input_data.split("-")
    username = command_parts[0]

    if len(command_parts) == 3:
        language = command_parts[1]
        points = int(command_parts[2])
        
        if language not in languages:
            languages[language] = 0
        
        languages[language] += 1
        
        if username not in users:
            users[username] = points
        else:
            if points > users[username]:
                users[username] = points
    else:
        users.pop(username)

    input_data = input()

new_line = "\n"

print("Results:")
[print(f"{k} | {v}") for k, v in users.items()]
print("Submissions:")
[print(f"{k} - {v}") for k, v in languages.items()]

# Old task condition for output:
#
# Print the exam results for each participant, ordered descending by max points and then by username.
# After that print each language, ordered descending by total submissions and then by language name.
#
# Solution for output according to the old condition
#
# users_sorted = {k: v for k, v in sorted(users.items(), key=lambda item: (-item[1], item[0]))}
# languages_sorted = {k: v for k, v in sorted(languages.items(), key=lambda item: (-item[1], item[0]))}
#
# print("Results:")
# [print(f"{k} | {v}") for k, v in users_sorted.items()]
# print("Submissions:")
# [print(f"{k} - {v}") for k, v in languages_sorted.items()]