def find_chars_between(first_char, second_char):
    chars = []

    for i in range(ord(first_char) + 1, ord(second_char)):
        chars.append(chr(i))

    return " ".join(chars)

first_char = input()
second_char = input()

print(find_chars_between(first_char, second_char))