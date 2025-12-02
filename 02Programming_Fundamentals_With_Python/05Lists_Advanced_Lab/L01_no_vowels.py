vowels = "aouei"

text = input()

print("".join([letter for letter in text if not letter.lower() in vowels]))