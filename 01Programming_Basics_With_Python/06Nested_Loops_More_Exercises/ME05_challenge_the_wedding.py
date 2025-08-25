men_count = int(input())
women_count = int(input())
tables_max_count = int(input())

for man in range(1, men_count + 1):
    for woman in range(1, women_count + 1):
        if tables_max_count > 0:
            print(f'({man} <-> {woman})', end=' ')
            tables_max_count -= 1
        else:
            break

    if tables_max_count == 0:
        break