input_line = input()

is_letter_c_used = False
is_letter_o_used = False
is_letter_n_used = False

result = ''
current_word = ''

while input_line != 'End':
    if not input_line.isalpha():
        input_line = input()
        continue

    if input_line == 'c':
        if not is_letter_c_used:
            is_letter_c_used = True
        else:
            current_word += input_line
    elif input_line == 'o':
        if not is_letter_o_used:
            is_letter_o_used = True
        else:
            current_word += input_line
    elif input_line == 'n':
        if not is_letter_n_used:
            is_letter_n_used = True
        else:
            current_word += input_line
    else:
        current_word += input_line

    if is_letter_c_used and is_letter_o_used and is_letter_n_used:
        result += current_word + ' '
        current_word = ''
        is_letter_c_used = False
        is_letter_o_used = False
        is_letter_n_used = False

    input_line = input()

print(result)