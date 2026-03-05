text = input()

index = 0

while True:
    index = text.find(":", index)
    if index == -1:
        break
    elif index < len(text) - 1:
        print(text[index:index+2])
        index += 1