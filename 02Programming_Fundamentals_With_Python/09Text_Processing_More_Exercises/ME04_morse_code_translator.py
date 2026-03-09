words = input().split(" | ")

morse_to_char = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

decoded_words = []

for word in words:
    decoded_word = "".join(morse_to_char[c] for c in word.split())
    decoded_words.append(decoded_word)

print(" ".join(decoded_words))