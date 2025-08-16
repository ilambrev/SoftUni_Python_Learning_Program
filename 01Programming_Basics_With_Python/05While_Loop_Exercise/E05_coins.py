from math import floor

change = float(input())
change = int(change * 100)

coins = 0

while change > 0:
    if change >= 200:
        current_coins = floor(change / 200)
        coins += current_coins
        change -= current_coins * 200
    elif change >= 100:
        current_coins = floor(change / 100)
        coins += current_coins
        change -= current_coins * 100
    elif change >= 50:
        current_coins = floor(change / 50)
        coins += current_coins
        change -= current_coins * 50
    elif change >= 20:
        current_coins = floor(change / 20)
        coins += current_coins
        change -= current_coins * 20
    elif change >= 10:
        current_coins = floor(change / 10)
        coins += current_coins
        change -= current_coins * 10
    elif change >= 5:
        current_coins = floor(change / 5)
        coins += current_coins
        change -= current_coins * 5
    elif change >= 2:
        current_coins = floor(change / 2)
        coins += current_coins
        change -= current_coins * 2
    elif change >= 1:
        current_coins = floor(change / 1)
        coins += current_coins
        change -= current_coins * 1

print(coins)