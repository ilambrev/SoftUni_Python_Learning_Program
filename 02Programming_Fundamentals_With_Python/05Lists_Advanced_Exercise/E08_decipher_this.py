from string import digits

words = input().split()

for i in range(len(words)):
    last_digit_index = [j for j in range(len(words[i])) if words[i][j] in digits][-1]

    decoded_word = chr(int(words[i][:last_digit_index+1])) + words[i][-1]
    if len(words[i][last_digit_index + 1:]) > 1:
        decoded_word += words[i][last_digit_index+2:-1] + words[i][last_digit_index+1]

    words[i] = decoded_word

print(" ".join(words))