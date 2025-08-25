start_letter = input()
end_letter = input()
omit_letter = input()

combination_counter = 0

for first_letter in range(ord(start_letter), ord(end_letter) + 1):
    if chr(first_letter) == omit_letter:
        continue

    for second_letter in range(ord(start_letter), ord(end_letter) + 1):
        if chr(second_letter) == omit_letter:
            continue

        for third_letter in range(ord(start_letter), ord(end_letter) + 1):
            if chr(third_letter) == omit_letter:
                continue

            combination_counter += 1

            print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=' ')

print(combination_counter)