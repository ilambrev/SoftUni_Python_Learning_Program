events = input().split("|")

energy = 100
coins = 100

for event in events:
    event, value = event.split("-")
    value = int(value)

    if event == "rest":
        gained_energy = value if energy + value <= 100 else 100 - energy
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy = energy + 50 if energy + 50 <= 100 else 100
            print("You had to rest!")
    else:
        if coins >= value:
            print(f"You bought {event}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {event}.")
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")