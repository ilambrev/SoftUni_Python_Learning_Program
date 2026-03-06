string = input()
result = ""
strength = 0

for i in range(len(string)):
    if string[i] == ">":
        strength += int(string[i+1])
        result += string[i]
    elif strength == 0:
        result += string[i]
    else:
        strength -= 1

print(result)