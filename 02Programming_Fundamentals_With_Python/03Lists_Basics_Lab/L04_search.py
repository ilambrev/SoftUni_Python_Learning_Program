n = int(input())
word = input()

strings = []

for _ in range(n):
    string = input()
    strings.append(string)

print(strings)

for i in range(len(strings) - 1, -1, -1):
    if not word in strings[i]:
        strings.pop(i)

print(strings)