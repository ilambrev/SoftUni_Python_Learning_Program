last_sector = input()
rows_in_first_sector = int(input())
odd_row_sits_count = int(input())

current_rows = rows_in_first_sector
even_row_sits_count = odd_row_sits_count + 2

total_sits_count = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, current_rows + 1):
        sits_count = odd_row_sits_count

        if row % 2 == 0:
            sits_count = even_row_sits_count

        for sit in range(ord('a'), ord('a') + sits_count):
            print(f'{chr(sector)}{row}{chr(sit)}')
            total_sits_count += 1

    current_rows += 1

print(total_sits_count)