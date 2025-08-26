a = int(input())
b = int(input())
generated_passwords_max_count = int(input())

first_symbol_begin = 35
first_symbol_end = 55
first_symbol_options = 1 + first_symbol_end - first_symbol_begin
second_symbol_begin = 64
second_symbol_end = 96
second_symbol_options = 1 + second_symbol_end - second_symbol_begin

passwords_counter = 0
is_passwords_limit_reached = False

for first_number in range(1, a + 1):
    for second_number in range(1, b + 1):

        if passwords_counter == generated_passwords_max_count:
            is_passwords_limit_reached = True
            break

        current_first_symbol = chr(first_symbol_begin
                                   + passwords_counter
                                   % first_symbol_options)
        current_second_symbol = chr(second_symbol_begin
                                    + passwords_counter
                                    % second_symbol_options)

        print(f'{current_first_symbol}{current_second_symbol}{first_number}{second_number}{current_second_symbol}{current_first_symbol}', end='|')

        passwords_counter += 1

    if is_passwords_limit_reached:
        break