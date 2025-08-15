money_for_trip = float(input())
money_available = float(input())

days_spending_money = 0
days = 0

while money_available < money_for_trip and days_spending_money < 5:
    action = input()
    money = float(input())

    days += 1

    if action == 'spend':
        days_spending_money += 1
        if money >= money_available:
            money_available = 0
        else:
            money_available -= money
    elif action == 'save':
        money_available += money
        days_spending_money = 0

if days_spending_money == 5:
    print("You can't save the money.")
    print(days)
elif money_available >= money_for_trip:
    print(f"You saved the money for {days} days.")