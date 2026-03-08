n = int(input())

for _ in range(n):
    text = input()
    i1 = text.find("@")
    i2 = text.find("|")
    i3 = text.find("#")
    i4 = text.find("*")

    print(f"{text[i1+1:i2]} is {text[i3+1:i4]} years old.")