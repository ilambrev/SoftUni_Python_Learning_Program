word = input()

reverced_word = ''

for i in range(len(word) - 1, -1, -1):
    reverced_word += word[i]

print(reverced_word)