string = input()

result = string[0] + "".join([string[i] for i in range(1, len(string)) if not string[i] == string[i-1]])

print(result)