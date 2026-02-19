n = int(input())

words = {}

for _ in range(n):
    word = input()
    synonym = input()

    if not word in words:
        words[word] = []

    words[word].append(synonym)

[print(f"{key} - {', '.join(value)}") for key, value in words.items()]