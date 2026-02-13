elements = input().split()
moves = 0
input_string = input()

while not input_string == "end":
    moves += 1
    i1, i2 = [int(i) for i in input_string.split()]

    if i1 < 0 or i1 > len(elements) - 1 or i2 < 0 or i2 > len(elements) - 1 or i1 == i2:
        print("Invalid input! Adding additional elements to the board")
        i = int(len(elements) / 2)
        elements.insert(i, f"-{moves}a")
        elements.insert(i + 1, f"-{moves}a")
    elif elements[i1] == elements[i2]:
        removed_element = elements.pop(max(i1, i2))
        elements.pop(min(i1, i2))
        print(f"Congrats! You have found matching elements - {removed_element}!")
    else:
        print("Try again!")
    
    if not elements:
        print(f"You have won in {moves} turns!")
        break

    input_string = input()
else:
    print(f"Sorry you lose :(\n{' '.join(elements)}")