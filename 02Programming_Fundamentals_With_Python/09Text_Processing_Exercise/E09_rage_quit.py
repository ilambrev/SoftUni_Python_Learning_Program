input_string = input()
unique_symbols = ""
current_string = ""
final_string = ""
current_number = ""
is_symbol_numeric = False


for symbol in input_string:
    symbol = symbol.upper()

    if not symbol.isnumeric() and is_symbol_numeric:
        final_string += current_string * int(current_number)
        current_string = ""
        current_number = ""
        is_symbol_numeric = False

    if symbol.isnumeric():
        current_number += symbol
        is_symbol_numeric = True
    else:
        current_string += symbol
        if symbol not in unique_symbols:
            unique_symbols += symbol

final_string += current_string * int(current_number)

print(f"Unique symbols used: {len(unique_symbols)}")
print(final_string)