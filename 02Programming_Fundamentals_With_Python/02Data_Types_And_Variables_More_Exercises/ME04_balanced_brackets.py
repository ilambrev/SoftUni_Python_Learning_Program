n = int(input())

result = "BALANCED"
open_brackets = 0

for _ in range(n):
    input_text = input()

    if input_text == "(":
        if open_brackets > 0:
            result = "UNBALANCED"
        elif open_brackets == 0:
            open_brackets += 1

    if input_text == ")":
        if open_brackets == 0:
            result = "UNBALANCED"
        elif open_brackets == 1:
            open_brackets -= 1

print(result)