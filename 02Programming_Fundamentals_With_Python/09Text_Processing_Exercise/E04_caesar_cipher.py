text = input()
step = 3
encrypted_text = ""

for symbol in text:
    symbol_value = ord(symbol)
    new_symbol = chr((symbol_value + step) % 128)
    encrypted_text += new_symbol

print(encrypted_text)