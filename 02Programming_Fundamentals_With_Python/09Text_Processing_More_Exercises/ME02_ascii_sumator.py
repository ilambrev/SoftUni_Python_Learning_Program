first_char_code = ord(input())
second_char_code = ord(input())
text = input()

sum = 0

for char in text:
    char_value = ord(char)
    if char_value in range(min(first_char_code, second_char_code) + 1, max(first_char_code, second_char_code)):
        sum += char_value

print(sum)