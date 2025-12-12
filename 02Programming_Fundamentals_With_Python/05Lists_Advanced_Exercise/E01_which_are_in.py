strings = input().split(", ")
text = input()

print([string for string in strings if string in text])