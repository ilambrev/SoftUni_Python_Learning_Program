number = int(input())

next_happy_year = number
is_year_happy = False

while not is_year_happy:
    next_happy_year += 1
    year_as_str = str(next_happy_year)

    for i in range(0, len(year_as_str) - 1):
        is_equality = False

        for j in range(i + 1, len(year_as_str)):
            if year_as_str[i] == year_as_str[j]:
                is_equality = True
                break

        if is_equality:
            break

    else:
        is_year_happy = True

print(next_happy_year)