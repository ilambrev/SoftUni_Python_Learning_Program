cards_string = input()
faro_shuffles_count = int(input())

deck = cards_string.split()

half = int(len(deck) / 2)

for _ in range(faro_shuffles_count):
    shufled_deck = [deck[0]]

    for i in range(1, half):
        shufled_deck.append(deck[half - 1 + i])
        shufled_deck.append(deck[i])

    shufled_deck.append(deck[-1])
    deck = shufled_deck

print(deck)