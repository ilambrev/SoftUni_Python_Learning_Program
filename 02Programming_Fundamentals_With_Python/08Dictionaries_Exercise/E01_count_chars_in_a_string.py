chars = [char for char in input() if not char == " "]
chars_occurrences = {}

for char in chars:
    if char not in chars_occurrences:
        chars_occurrences[char] = 0
    
    chars_occurrences[char] += 1

[print(f"{key} -> {value}") for key, value in chars_occurrences.items()]