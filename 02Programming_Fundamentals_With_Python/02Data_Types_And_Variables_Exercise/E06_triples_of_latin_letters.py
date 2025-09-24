from string import ascii_lowercase

letters_count = int(input())

for i in range(letters_count):
    for j in range(letters_count):
        for k in range(letters_count):
            print(f'{ascii_lowercase[i]}{ascii_lowercase[j]}{ascii_lowercase[k]}')