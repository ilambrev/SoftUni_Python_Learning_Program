from string import ascii_uppercase

text = input()

indexes = []

for i in range(len(text)):
    if text[i] in ascii_uppercase:
        indexes.append(i)

print(indexes)