usernames = input().split(", ")

for username in usernames:
    is_length_right = 3 <= len(username) <= 16
    contains_right_symbols = True

    for symbol in username:
        if not symbol.isalpha() and not symbol.isdigit() and not symbol == "_" and not symbol == "-":
            contains_right_symbols = False
            break

    if is_length_right and contains_right_symbols:
        print(username)