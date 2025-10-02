group_size = int(input())
days = int(input())

profit = 0
spendings = 0
current_group_size = group_size

for day in range(1, days + 1):
    profit += 50

    if day % 10 == 0:
        current_group_size -= 2

    if day % 15 == 0:
        current_group_size += 5

    spendings += current_group_size * 2

    if day % 3 == 0 and day % 5 == 0:
        spendings += current_group_size * 2

    if day % 3 == 0:
        spendings += current_group_size * 3

    if day % 5 == 0:
        profit += current_group_size * 20

coins_per_companion = 0

if profit > spendings and current_group_size > 0:
    coins_per_companion = int((profit - spendings) / current_group_size)

print(f'{current_group_size} companions received {coins_per_companion} coins each.')