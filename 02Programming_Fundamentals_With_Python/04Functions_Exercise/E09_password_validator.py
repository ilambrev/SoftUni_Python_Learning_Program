from string import ascii_letters, digits

def validate_password(password):
    is_valid = True

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    is_composed_of_digits_and_letters = True
    digits_count = 0

    for symbol in password:
        if not symbol in ascii_letters and not symbol in digits:
            is_composed_of_digits_and_letters = False

        if symbol in digits:
            digits_count += 1

    if not is_composed_of_digits_and_letters:
        print("Password must consist only of letters and digits")
        is_valid = False

    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


password = input()

validate_password(password)