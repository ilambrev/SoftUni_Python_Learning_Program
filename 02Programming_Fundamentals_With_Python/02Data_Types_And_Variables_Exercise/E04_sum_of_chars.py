lines_count = int(input())

chars_values_sum = 0

for _ in range(lines_count):
    char = input()
    chars_values_sum += ord(char)

print(f'The sum equals: {chars_values_sum}')