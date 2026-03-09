keys = [int(n) for n in input().split()]

def decrypt_message(message, keys):
    decrypted_message = ""

    for i in range(len(message)):
        keys_index = i % len(keys)
        key = keys[keys_index]
        symbol = message[i]

        decrypted_message += chr(ord(symbol) - key)

    return decrypted_message

def find_separator_indexes(separator, message):
    indexes = []
    start_index = 0

    while True:
        index = message.find(separator, start_index)

        if index > -1:
            indexes.append(index)
            start_index = index + 1
        else:
            break

    return indexes


input_line = input()

while not input_line == "find":
    decrypted_message = decrypt_message(input_line, keys)
    i1, i2 = find_separator_indexes("&", decrypted_message)
    treasure_type = decrypted_message[i1+1:i2]
    i1 = find_separator_indexes("<", decrypted_message)[0]
    i2 = find_separator_indexes(">", decrypted_message)[0]
    coordinates = decrypted_message[i1+1:i2]
    print(f"Found {treasure_type} at {coordinates}")

    input_line = input()